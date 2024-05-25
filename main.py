from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

class SimpleAnimationApp(App):
    def build(self):
        layout = FloatLayout()

        # Кнопка, по нажатии на которую начнется анимация
        button = Button(text='Запустить анимацию', size_hint=(None, None), pos=(200, 300))
        button.bind(on_press=self.start_animation)
        layout.add_widget(button)

        # Объект, который будет анимироваться (картинка)
        animated_image = Image(source='C:/Users/hwaya/PyCharmProjects/33pr/icon.jpg', size_hint=(None, None), pos=(100, 100))
        layout.add_widget(animated_image)

        self.animated_image = animated_image

        return layout

    def start_animation(self, instance):
        # Создаем анимацию для изменения позиции объекта
        animation = Animation(pos=(500, 500), duration=2) + Animation(pos=(100, 100), duration=2)
        animation.repeat = True

        # Запускаем анимацию для объекта
        animation.start(self.animated_image)

if __name__ == '__main__':
    SimpleAnimationApp().run()