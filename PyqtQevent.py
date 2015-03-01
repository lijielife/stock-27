"""pyqt4 qevent string dict

Constant	    Value	Description
Qt.white	    3	White (#ffffff)
Qt.black	    2	Black (#000000)
Qt.red	        7	Red (#ff0000)
Qt.darkRed	    13	Dark red (#800000)
Qt.green	    8	Green (#00ff00)
Qt.darkGreen	14	Dark green (#008000)
Qt.blue	        9	Blue (#0000ff)
Qt.darkBlue	    15	Dark blue (#000080)
Qt.cyan	        10	Cyan (#00ffff)
Qt.darkCyan	    16	Dark cyan (#008080)
Qt.magenta	    11	Magenta (#ff00ff)
Qt.darkMagenta	17	Dark magenta (#800080)
Qt.yellow	    12	Yellow (#ffff00)
Qt.darkYellow	18	Dark yellow (#808000)
Qt.gray	        5	Gray (#a0a0a4)
Qt.darkGray	    4	Dark gray (#808080)
Qt.lightGray	6	Light gray (#c0c0c0)
Qt.transparent	19	a transparent black value (i.e., QColor(0, 0, 0, 0))
Qt.color0	    0	0 pixel value (for bitmaps)
Qt.color1	    1	1 pixel value (for bitmaps)
"""
eventStr={
    0:"QEvent.None",
    130:"QEvent.AccessibilityDescription",
    119:"QEvent.AccessibilityHelp",
    86:"QEvent.AccessibilityPrepare",
    114:"QEvent.ActionAdded",
    113:"QEvent.ActionChanged",
    115:"QEvent.ActionRemoved",
    99:"QEvent.ActivationChange",
    121:"QEvent.ApplicationActivate",
    122:"QEvent.ApplicationDeactivate",
    36:"QEvent.ApplicationFontChange",
    37:"QEvent.ApplicationLayoutDirectionChange",
    38:"QEvent.ApplicationPaletteChange",
    35:"QEvent.ApplicationWindowIconChange",
    68:"QEvent.ChildAdded",
    70:"QEvent.ChildInserted",
    69:"QEvent.ChildPolished",
    71:"QEvent.ChildRemoved",
    40:"QEvent.Clipboard",
    19:"QEvent.Close",
    200:"QEvent.CloseSoftwareInputPanel",
    178:"QEvent.ContentsRectChange",
    82:"QEvent.ContextMenu",
    183:"QEvent.CursorChange",
    52:"QEvent.DeferredDelete",
    60:"QEvent.DragEnter",
    62:"QEvent.DragLeave",
    61:"QEvent.DragMove",
    63:"QEvent.Drop",
    98:"QEvent.EnabledChange",
    10:"QEvent.Enter",
    150:"QEvent.EnterEditFocus",
    124:"QEvent.EnterWhatsThisMode",
    116:"QEvent.FileOpen",
    8:"QEvent.FocusIn",
    9:"QEvent.FocusOut",
    97:"QEvent.FontChange",
    188:"QEvent.GrabKeyboard",
    186:"QEvent.GrabMouse",
    159:"QEvent.GraphicsSceneContextMenu",
    164:"QEvent.GraphicsSceneDragEnter",
    166:"QEvent.GraphicsSceneDragLeave",
    165:"QEvent.GraphicsSceneDragMove",
    167:"QEvent.GraphicsSceneDrop",
    163:"QEvent.GraphicsSceneHelp",
    160:"QEvent.GraphicsSceneHoverEnter",
    162:"QEvent.GraphicsSceneHoverLeave",
    161:"QEvent.GraphicsSceneHoverMove",
    158:"QEvent.GraphicsSceneMouseDoubleClick",
    155:"QEvent.GraphicsSceneMouseMove",
    156:"QEvent.GraphicsSceneMousePress",
    157:"QEvent.GraphicsSceneMouseRelease",
    182:"QEvent.GraphicsSceneMove",
    181:"QEvent.GraphicsSceneResize",
    168:"QEvent.GraphicsSceneWheel",
    18:"QEvent.Hide",
    27:"QEvent.HideToParent",
    127:"QEvent.HoverEnter",
    128:"QEvent.HoverLeave",
    129:"QEvent.HoverMove",
    96:"QEvent.IconDrag",
    101:"QEvent.IconTextChange",
    83:"QEvent.InputMethod",
    6:"QEvent.KeyPress",
    7:"QEvent.KeyRelease",
    89:"QEvent.LanguageChange",
    90:"QEvent.LayoutDirectionChange",
    76:"QEvent.LayoutRequest",
    11:"QEvent.Leave",
    151:"QEvent.LeaveEditFocus",
    125:"QEvent.LeaveWhatsThisMode",
    88:"QEvent.LocaleChange",
    176:"QEvent.NonClientAreaMouseButtonDblClick",
    174:"QEvent.NonClientAreaMouseButtonPress",
    175:"QEvent.NonClientAreaMouseButtonRelease",
    173:"QEvent.NonClientAreaMouseMove",
    177:"QEvent.MacSizeChange",
    153:"QEvent.MenubarUpdated",
    43:"QEvent.MetaCall",
    102:"QEvent.ModifiedChange",
    4:"QEvent.MouseButtonDblClick",
    2:"QEvent.MouseButtonPress",
    3:"QEvent.MouseButtonRelease",
    5:"QEvent.MouseMove",
    109:"QEvent.MouseTrackingChange",
    13:"QEvent.Move",
    12:"QEvent.Paint",
    39:"QEvent.PaletteChange",
    131:"QEvent.ParentAboutToChange",
    21:"QEvent.ParentChange",
    212:"QEvent.PlatformPanel",
    75:"QEvent.Polish",
    74:"QEvent.PolishRequest",
    123:"QEvent.QueryWhatsThis",
    199:"QEvent.RequestSoftwareInputPanel",
    14:"QEvent.Resize",
    117:"QEvent.Shortcut",
    51:"QEvent.ShortcutOverride",
    17:"QEvent.Show",
    26:"QEvent.ShowToParent",
    50:"QEvent.SockAct",
    192:"QEvent.StateMachineSignal",
    193:"QEvent.StateMachineWrapped",
    112:"QEvent.StatusTip",
    100:"QEvent.StyleChange",
    87:"QEvent.TabletMove",
    92:"QEvent.TabletPress",
    93:"QEvent.TabletRelease",
    94:"QEvent.OkRequest",
    171:"QEvent.TabletEnterProximity",
    172:"QEvent.TabletLeaveProximity",
    1:"QEvent.Timer",
    120:"QEvent.ToolBarChange",
    110:"QEvent.ToolTip",
    184:"QEvent.ToolTipChange",
    189:"QEvent.UngrabKeyboard",
    187:"QEvent.UngrabMouse",
    78:"QEvent.UpdateLater",
    77:"QEvent.UpdateRequest",
    111:"QEvent.WhatsThis",
    118:"QEvent.WhatsThisClicked",
    31:"QEvent.Wheel",
    132:"QEvent.WinEventAct",
    24:"QEvent.WindowActivate",
    103:"QEvent.WindowBlocked",
    25:"QEvent.WindowDeactivate",
    34:"QEvent.WindowIconChange",
    105:"QEvent.WindowStateChange",
    33:"QEvent.WindowTitleChange",
    104:"QEvent.WindowUnblocked",
    126:"QEvent.ZOrderChange",
    169:"QEvent.KeyboardLayoutChange",
    170:"QEvent.DynamicPropertyChange",
    194:"QEvent.TouchBegin",
    195:"QEvent.TouchUpdate",
    196:"QEvent.TouchEnd",
    203:"QEvent.WinIdChange",
    198:"QEvent.Gesture",
    202:"QEvent.GestureOverride",
    }
