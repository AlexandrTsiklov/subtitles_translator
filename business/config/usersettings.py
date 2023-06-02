# толщина букв субтитров
FONT_THICKNESS = 2

# размер шрифта субтитров
FONT_SCALE = 1.1

# цвет субтитров
FONT_COLOR = (190, 210, 210)

# обводки нет, так что неважно
LINE_THICKNESS = 1

# если на сайте меняется размер субтитров, нужно регулировать этот коэф
LINE_HEIGHT_ADJUST_COEFFICIENT = 0.97

# шарина рамки, в которой отображаются субтитры
LINE_WIDTH_LIMIT = 0.5

# ширина пользовательского экрана (лучше не трогать(
SCREEN_WIDTH = 1920

# высота пользовательского экрана
SCREEN_HEIGHT = 1080

# координата y, где по умолчанию будут отображаться субтитры (если не использовать ручное выделение)
DEFAULT_SUBTITLES_DST = int(SCREEN_HEIGHT * 0.7)

# координаты углов рамки, в которую должны попасть субтитры для перевода (если не использовать ручное выделение)
X1_DEFAULT = 460
Y1_DEFAULT = 760
X2_DEFAULT = 1460
Y2_DEFAULT = 930
X_DEFAULT_DST = min(X1_DEFAULT, X2_DEFAULT)
Y_DEFAULT_DST = min(Y1_DEFAULT, Y2_DEFAULT)
WIDTH_DEFAULT = abs(X1_DEFAULT - X2_DEFAULT)
HEIGHT_DEFAULT = abs(Y1_DEFAULT - Y2_DEFAULT)