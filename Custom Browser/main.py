import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize bookmarks and history lists
        self.bookmarks = []
        self.history = []

        # Set up the tab widget to manage browser tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.new_tab("https://google.com")  # Open Google in the first tab

        # Create the navigation bar (toolbar)
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.current_browser().back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.current_browser().forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.current_browser().reload)
        navbar.addAction(reload_btn)

        # Home button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL bar for entering website addresses
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Set custom styles for the application
        self.setStyleSheet("""
            QToolBar { background-color: #2E3440; color: white; }
            QLineEdit { background-color: #3B4252; color: white; }
        """)

        # Update URL bar when the tab or browser content changes
        self.tabs.currentChanged.connect(self.update_url)
        self.current_browser().urlChanged.connect(self.update_url)

    def current_browser(self):
        # Get the currently active browser tab
        return self.tabs.currentWidget()

    def new_tab(self, url=None):
        # Open a new tab with the given URL
        browser = QWebEngineView()
        if url:
            browser.setUrl(QUrl(url))
        else:
            browser.setUrl(QUrl("https://google.com"))
        self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentWidget(browser)

    def navigate_home(self):
        # Navigate to the home page (Google)
        self.current_browser().setUrl(QUrl("https://google.com"))

    def navigate_to_url(self):
        # Navigate to the URL entered in the URL bar
        try:
            url = self.url_bar.text()
            self.current_browser().setUrl(QUrl(url))
            self.history.append(url)  # Add to browsing history
        except Exception as e:
            print(f"Error loading URL: {e}")

    def update_url(self, q=None):
        # Update the URL bar with the current tab's URL
        if q:
            self.url_bar.setText(q.toString())
        else:
            self.url_bar.setText(self.current_browser().url().toString())

    def add_bookmark(self):
        # Add the current URL to bookmarks
        url = self.current_browser().url().toString()
        self.bookmarks.append(url)
        print("Bookmark added:", url)

# Set platform for PyQt compatibility (Debian fix)
os.environ['QT_QPA_PLATFORM'] = 'xcb'

# Create the application instance and main window
app = QApplication(sys.argv)
QApplication.setApplicationName("Custom Browser")
window = MainWindow()
window.show()

# Start the event loop
sys.exit(app.exec_())
