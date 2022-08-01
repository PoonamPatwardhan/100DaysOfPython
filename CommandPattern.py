class Screen:
    def __init__(self, text, start =0, end=0):
        self.text = text
        self.clipBoard = ''
        self.previous_state = self.text
        self.start = start
        self.end = end

    def __str__(self):
        print(self.text);

class ScreenCommand:
    def __init__(self, screen):
        self.screen = screen

    def execute(self):
        pass

    def undo(self):
        pass


class CutCommand(ScreenCommand):
    def __init__(self, screen, start, end):
        super().__init__(screen)
        self.start = start
        self.end = end
        self.screen.start = start
        self.screen.end = end

    def execute(self):
        self.screen.previous_state = self.screen.text
        self.screen.clipBoard = self.screen.text[self.start:self.end]
        self.screen.text = self.screen.text[:self.start] + self.screen.text[self.end:]

    def undo(self):
        self.screen.clipBoard = ''
        self.screen.text = self.screen.previous_state

class PasteCommand(ScreenCommand):
    def __init__(self, screen, offset):
        super().__init__(screen)
        self.offset = offset

    def execute(self):
        self.screen.previous_state = self.screen.text
        self.screen.text = self.screen.text[:self.offset] + self.screen.clipBoard + self.screen.text[self.offset:]

    def undo(self):
        #self.screen.clipBoard = ''
        self.screen.text = self.screen.previous_state


class Invoker:
    def __init__(self):
        self.commands = []

    def store_and_execute(self, screenCommand):
        screenCommand.execute()
        self.commands.append(screenCommand)

    def undo_last(self):
        self.commands.pop().undo()


if __name__ == '__main__':
    screen = Screen("Hello World");
    screen.__str__();
    cutCmd = CutCommand(screen, 5, 11);
    pasteCmd = PasteCommand(screen,0);
    screenInvoker = Invoker();
    screenInvoker.store_and_execute(cutCmd);
    screen.__str__();
    screenInvoker.store_and_execute(pasteCmd);
    screen.__str__();
    screenInvoker.undo_last()
    screen.__str__();

