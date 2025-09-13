#!/usr/bin/python3
# coding = UTF-8
'''
一个可以自由操控字体的Python库
from: shufeng2012
'''

class Font:
    '''
    自定义字体的类
    '''

    STOP: str = "\033[0m"

    class Fore:
        # 字体颜色
        BLACK: str = "30"
        RED: str = "31"
        GREEN: str = "32"
        BROWN: str = "33"
        BLUE: str = "34"
        PURPLE: str = "35"
        CYAN: str = "36"
        GRAY: str = "37"

    class Back:
        # 背景颜色
        BLACK: str = "40"
        RED: str = "41"
        GREEN: str = "42"
        BROWN: str = "43"
        BLUE: str = "44"
        PURPLE: str = "45"
        CYAN: str = "46"
        WHITE: str = "47"

    class Variant:
        # 字体变体
        HIGHLIGHT: str = "1"
        LOWLIGHT: str = "2"
        ITALIC: str = "3"
        UNDERLINE: str = "4"
        FLASHING: str = "5"
        REVERSE_DISPLAY: str = "6"
        BLANKING: str = "8"

    def color(self, string: str, Fore: str = "", Back: str = None, Reset: bool = True) -> str:
        '''
        处理字符串颜色
        '''
        return_string: str          # 返回处理后的字符串
        ForeGround: str             # 前景色
        BackGround: str             # 背景色
        ForeGround = f"\033[0;{Fore}m"
        BackGround = f"\033[0;{Back}m"

        if Back == None:             # 无背景
            return_string = ForeGround + string
        else:                       # 有背景
            if Fore == "":
                return_string = BackGround + string
            else:
                return_string = BackGround + ForeGround + string
        if Reset == True:           # 是否重置
            return_string += self.STOP

        return return_string

    def variant(self, string: str, highlight: bool = False, lowlight: bool = False, italic: bool = False, underline: bool = False, flashing: bool = False, reverse_display: bool = False, blanking: bool = False, reset: bool = True) -> str:
        '''
        处理字符串变体
        '''
        return_string: str = string     # 返回处理后的字符串
        variant: str

        if highlight == True:               # 高亮
            variant = f"\033[{self.Variant.HIGHLIGHT}m"
        elif lowlight == True:              # 低亮
            variant = f"\033[{self.Variant.LOWLIGHT}m"
        elif italic == True:                # 斜体
            variant = f"\033[{self.Variant.ITALIC}m"
        elif underline == True:             # 下划线
            variant = f"\033[{self.Variant.UNDERLINE}m"
        elif flashing == True:              # 闪烁
            variant = f"\033[{self.Variant.FLASHING}m"
        elif reverse_display == True:       # 反显
            variant = f"\033[{self.Variant.REVERSE_DISPLAY}m"
        elif blanking == True:              # 消隐
            variant = f"\033[{self.Variant.BLANKING}m"
        else:
            variant = f"\033[0m"
        return_string = variant + string
        if reset == True:                   # 是否重置
            return_string += self.STOP

        return return_string

    def __init__(self, string: str = None, Fore: str = "", Back: str = None, highlight: bool = False, lowlight: bool = False, italic: bool = False, underline: bool = False, flashing: bool = False, reverse_display: bool = False, blanking: bool = False, reset: bool = True) -> None:
        '''
        构造函数
        '''
        return_string: str          # 返回的处理后的字符串
        ansi: str                   # ANSI转义序列

        if highlight == True:               # 高亮
            ansi = f"\033[{self.Variant.HIGHLIGHT};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.HIGHLIGHT};{Back}m\033[{self.Variant.HIGHLIGHT};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.HIGHLIGHT};{Back}m"
        elif lowlight == True:               # 低亮
            ansi = f"\033[{self.Variant.LOWLIGHT};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.LOWLIGHT};{Back}m\033[{self.Variant.LOWLIGHT};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.LOWLIGHT};{Back}m"
        elif italic == True:               # 斜体
            ansi = f"\033[{self.Variant.ITALIC};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.ITALIC};{Back}m\033[{self.Variant.ITALIC};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.ITALIC};{Back}m"
        elif underline == True:               # 下划线
            ansi = f"\033[{self.Variant.UNDERLINE};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.UNDERLINE};{Back}m\033[{self.Variant.UNDERLINE};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.UNDERLINE};{Back}m"
        elif flashing == True:               # 闪烁
            ansi = f"\033[{self.Variant.FLASHING};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.FLASHING};{Back}m\033[{self.Variant.FLASHING};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.FLASHING};{Back}m"
        elif reverse_display == True:               # 反显
            ansi = f"\033[{self.Variant.REVERSE_DISPLAY};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.REVERSE_DISPLAY};{Back}m\033[{self.Variant.REVERSE_DISPLAY};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.REVERSE_DISPLAY};{Back}m"
        elif blanking == True:               # 闪烁
            ansi = f"\033[{self.Variant.BLANKING};"
            if Fore != "":           # 不为空
                if Back == None:            # 无背景
                    ansi += f"{Fore}m"
                else:                       # 有背景
                    ansi = f"\033[{self.Variant.BLANKING};{Back}m\033[{self.Variant.BLANKING};{Fore}m"
            else:                           # 为空
                ansi = f"\033[{self.Variant.BLANKING};{Back}m"
        else:                               # 无选项
            if Back == None:                # 无背景
                ansi = f"\033[0;{Fore}m"
            else:                           # 有背景
                if Fore != "":
                    ansi = f"\033[0;{Back}m\033[0;{Fore}m"
                else:
                    ansi = f"\033[0;{Back}m"
        return_string = ansi + string
        if reset == True:                   # 是否重置
            return_string += self.STOP


        print(return_string)
