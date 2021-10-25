class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化信息。"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        # 任何情况下都不应该重置最高得分
        with open('score.txt', 'r') as file:
            self.high_score = int(file.readline())


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
