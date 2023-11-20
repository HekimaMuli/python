class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    """
    Creates new Television instance
    """
    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    """
    Turns Television power off/on
    """
    def power(self) -> None:
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    """
    Mutes/unmutes Television if power is on
    """
    def mute(self) -> None:
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MAX_VOLUME
            else:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME

    """
    Increases Television channel if power is on
    """
    def channel_up(self) -> None:
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    """
    Decreases Television channel if power is on
    """
    def channel_down(self) -> None:
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    """
    Increases Television volume if power is on
    Also unmutes Television
    """
    def volume_up(self) -> None:
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MAX_VOLUME:
                return
            else:
                self.__volume += 1

    """
    Decreases Television volume if power is on
    Also unmutes Television
    """
    def volume_down(self) -> None:
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MIN_VOLUME:
                return
            else:
                self.__volume -= 1

    """
    Overrides print string returned for Television
    return: Television status
    """
    def __str__(self) -> str:
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'