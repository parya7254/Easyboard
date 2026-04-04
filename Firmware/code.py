import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros, Delay
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

mousekeys = MouseKeys(
    max_speed=10,
    acc_interval=100,
    move_step=0.6
)

keyboard.modules.append(MouseKeys())

keyboard.col_pins=(board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,  board.GP15, board.GP16, board.GP20, board.GP21, board.GP22, board.GP23, board.GP28, board.GP29)
keyboard.row_pins=(board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)
keyboard.diode_orientation=DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

rgb=RGB(pixel_pin=board.GP0, num_pixels=96)
keyboard.extensions.append(rgb)

i2c_bus = busio.I2C(board.GP27, board.GP26)
diplay_driver=SSD1306(
    i2c=i2c_bus
)

display=Display(
    display=display_driver,
    entries=[
        TextEntry('Mode: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='Key Shortcuts', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='Mouse', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='RGB Animations', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='RGB Controls', x=40, y=32, y_anchor='B', layer=3),
        TextEntry(text='0 1 2 3', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=12, y=4, inverted=True, layer=2),
        TextEntry(text='3', x=12, y=4, inverted=True, layer=3),
    ],

    width=128,
    height=64,
    dim_time=4,
    dim_target=0,
    off_time=10,
    brightness=1,
)

keyboard.extensions.append(display)

keyboard.modules.append(Macros())

MENU=KC.MACRO(
    Press(KC.LSHIFT)
    Tap(KC.F10)
    Release(KC.SHIFT)
)

COPY = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

PASTE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

CUT = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.X),
    Release(KC.LCTL)
)

UNDO = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Z),
    Release(KC.LCTL)
)
REDO = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.LSFT),
    Tap(KC.Z),
    Release(KC.LSFT),
    Release(KC.LCTL)
)

REDO2 = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Y),
    Release(KC.LCTL)
)

NEXTWINDOW = KC.MACRO(
    Press(KC.LALT),
    Tap(KC.TAB),
    Release(KC.LALT)
)

LASTWINDOW = KC.MACRO(
    Press(KC.LALT),
    Press(KC.LSHIFT),
    Tap(KC.TAB),
    Release(KC.LSHIFT),
    Release(KC.LALT)
)

L0= KC.DF(0)
L1= KC.DF(1)
L2= KC.DF(2)
L3= KC.DF(3)

keyboard.keymap = [
    # Layer 0
    {
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.INSERT, KC.HOME,
        KC.PGUP, KC.TAB, KC.Q, KC.W, KC.E, KC.T, KC.Y, KC.U, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE,
        KC.END, KC.PGDOWN, KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.LSHIFT,
        KC.Z, KC.X, KC.C, KC.V, KC.B KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.LCTRL, KC.LWIN, KC.LALT, KC.SPACE,
        KC.RALT, KC.RGUI, MENU, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, COPY, PASTE, CUT, UNDO, REDO, REDO2, NEXTWINDOW, LASTWINDOW, L1,

    }
    # Layer 1
    {
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.INSERT, KC.HOME,
        KC.PGUP, KC.TAB, KC.Q, KC.W, KC.E, KC.T, KC.Y, KC.U, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE,
        KC.END, KC.PGDOWN, KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.LSHIFT,
        KC.Z, KC.X, KC.C, KC.V, KC.B KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.LCTRL, KC.LWIN, KC.LALT, KC.SPACE,
        KC.RALT, KC.RGUI, MENU, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.MB_LMB,  KC.MS_UP,  KC.MB_RMB,  KC.MS_LEFT, KC.MS_DOWN, KC.MS_RIGHT, KC.NO, KC.MS_DOWN, L2,

    }
    # Layer 2
    {
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.INSERT, KC.HOME,
        KC.PGUP, KC.TAB, KC.Q, KC.W, KC.E, KC.T, KC.Y, KC.U, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE,
        KC.END, KC.PGDOWN, KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.LSHIFT,
        KC.Z, KC.X, KC.C, KC.V, KC.B KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.LCTRL, KC.LWIN, KC.LALT, KC.SPACE,
        KC.RALT, KC.RGUI, MENU, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,  KC.RGB_MODE_BREATHE_RAINBOW,  KC.RGB_MODE_RAINBOW, KC.RGB_MODE_BREATHE, KC.RGB_MODE_PLAIN, KC.RGB_ANI, KC.RGB_AND, L2,

    }
    # Layer 3
    {
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.INSERT, KC.HOME,
        KC.PGUP, KC.TAB, KC.Q, KC.W, KC.E, KC.T, KC.Y, KC.U, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.DELETE,
        KC.END, KC.PGDOWN, KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.LSHIFT,
        KC.Z, KC.X, KC.C, KC.V, KC.B KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.LCTRL, KC.LWIN, KC.LALT, KC.SPACE,
        KC.RALT, KC.RGUI, MENU, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.RGB_TOG, KC.RGB_HUI, KC.RGB_HUD, KC.RGB_SAI, KC.RGB_SAD, KC.RGB_VAI, KC.RGB_VAD, KC.RGB_MODE_PLAIN, L3,

    }
]

if __name__ == '__main__':
    keyboard.go()