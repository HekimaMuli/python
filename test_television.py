import unittest
from television import Television


class MyTestCase(unittest.TestCase):

    def test_init(self):
        self.tv = Television()

        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

    def test_power(self):
        self.tv = Television()

        self.tv.power()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.power()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

    def test_mute(self):
        self.tv = Television()

        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.mute()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 2')

        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = 2')

        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

    def test_channel_up(self):
        self.tv = Television()

        self.tv.channel_up()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = 1, Volume = {Television.MIN_VOLUME}')

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

    def test_channel_down(self):
        self.tv = Television()

        self.tv.channel_down()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.power()
        self.tv.channel_down()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}')

    def test_volume_up(self):
        self.tv = Television()

        self.tv.volume_up()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 1')

        self.tv.mute()
        self.tv.volume_up()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 2')

        self.tv.volume_up()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MAX_VOLUME}')

    def test_volume_down(self):
        self.tv = Television()

        self.tv.volume_down()
        self.assertEqual(self.tv.__str__(), f'Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}')

        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 1')

        self.tv.mute()
        self.tv.volume_down()
        self.assertEqual(self.tv.__str__(), f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 1')


if __name__ == '__main__':
    unittest.main()
