# PySide6 기반 I/O Manager 샘플 UI

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit,
    QTableWidget, QTableWidgetItem, QCheckBox, QComboBox, QHBoxLayout,
    QVBoxLayout, QFileDialog, QGridLayout
)
import sys

class IOManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("I/O Manager")
        self.setMinimumSize(900, 600)

        # 메인 위젯 및 레이아웃 설정
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # --- 경로 선택 영역 ---
        path_layout = QHBoxLayout()

        self.path_label = QLabel("Path :")
        self.path_field = QLineEdit("/show/Constantine/product/scan/20241226_2/s030_0840")
        self.path_hint = QLabel(" => /show/{project}/product/scan/{scan_version}/{seq_name}_{shot_num}")
        self.select_btn = QPushButton("Select")
        self.load_btn = QPushButton("Load")

        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_field, 3)
        path_layout.addWidget(self.path_hint, 4)
        path_layout.addWidget(self.select_btn)
        path_layout.addWidget(self.load_btn)

        # --- 옵션 영역 ---
        options_layout = QHBoxLayout()
        self.check_nonretime = QCheckBox("Non Retime")
        self.check_mov2dpx = QCheckBox("MOV to DPX")
        self.check_clplib = QCheckBox("ClipLib")
        self.colorspace_dropdown = QComboBox()
        self.colorspace_dropdown.addItems(["rec709", "ACEScg", "sRGB"])

        options_layout.addWidget(self.check_nonretime)
        options_layout.addWidget(self.check_mov2dpx)
        options_layout.addWidget(self.check_clplib)
        options_layout.addWidget(QLabel("Colorspace"))
        options_layout.addWidget(self.colorspace_dropdown)

        # --- 테이블 영역 ---
        self.table = QTableWidget(10, 5)  # (row, col) 초기값 하드코딩
        self.table.setHorizontalHeaderLabels(["Frame", "Timecode", "Clip Name", "Slate", "Note"])

        # --- 하단 Excel, Validate, Action 영역 ---
        bottom_layout = QHBoxLayout()

        # Excel 관련
        excel_layout = QVBoxLayout()
        excel_layout.addWidget(QLabel("Excel"))
        self.btn_edit = QPushButton("Edit")
        self.btn_save = QPushButton("Save")
        excel_layout.addWidget(self.btn_edit)
        excel_layout.addWidget(self.btn_save)

        # Validate 관련
        validate_layout = QVBoxLayout()
        validate_layout.addWidget(QLabel("Validate"))
        self.btn_timecode = QPushButton("Timecode")
        self.btn_version = QPushButton("Version")
        self.btn_src_version = QPushButton("Src Version")
        self.btn_shot_editorial = QPushButton("Shot for Editorial")
        validate_layout.addWidget(self.btn_timecode)
        validate_layout.addWidget(self.btn_version)
        validate_layout.addWidget(self.btn_src_version)
        validate_layout.addWidget(self.btn_shot_editorial)

        # Action 관련
        action_layout = QVBoxLayout()
        action_layout.addWidget(QLabel("Action"))
        self.btn_collect = QPushButton("Collect")
        self.btn_publish = QPushButton("Publish")
        action_layout.addWidget(self.btn_collect)
        action_layout.addWidget(self.btn_publish)

        # 하단 결합
        bottom_layout.addLayout(excel_layout)
        bottom_layout.addLayout(validate_layout)
        bottom_layout.addLayout(action_layout)

        # 전체 레이아웃 구성
        main_layout.addLayout(path_layout)
        main_layout.addLayout(options_layout)
        main_layout.addWidget(self.table)
        main_layout.addLayout(bottom_layout)

        # --- 시그널 연결 (예시용 하드코딩 동작) ---
        self.select_btn.clicked.connect(self.select_path)
        self.load_btn.clicked.connect(self.load_metadata)

    def select_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.path_field.setText(folder)

    def load_metadata(self):
        # 예시: 테이블에 하드코딩된 값 채우기
        data = [
            ("0000001", "01:00:00:01", "Clip_A", "Slate01", "Good"),
            ("0000002", "01:00:00:02", "Clip_A", "Slate01", "Blur")
        ]
        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(val))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = IOManagerWindow()
    win.show()
    sys.exit(app.exec())
