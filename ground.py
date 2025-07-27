from turtle import Turtle

class Ground():
    def __init__(self):
        self.ground = []
        self.blocks = []  
        self.create_ground()

    def create_ground(self):
        x_start = -200
        x_end = 200
        y = -280
        self.ground = [(x, y) for x in range(x_start, x_end + 1, 20)]

    def add_shapes(self, figurka):
        for block in figurka.figurka:
            self.ground.append((block.xcor(), block.ycor()))
            self.blocks.append(block) 
        
        y_levels = {}
        for pos in self.ground:
            if isinstance(pos, tuple) and pos[1] > -280:
                y = pos[1]
                if y not in y_levels:
                    y_levels[y] = []
                y_levels[y].append(pos[0])
        
        
        self.clear_lines()

    def clear_lines(self):
        y_coords = set()
        for pos in self.ground:
            if isinstance(pos, tuple) and pos[1] > -280: 
                y_coords.add(pos[1])
        
        lines_to_clear = []
        
        for y in y_coords:
            blocks_in_line = [pos for pos in self.ground if isinstance(pos, tuple) and pos[1] == y]
            x_positions = [pos[0] for pos in blocks_in_line]
            expected_positions = list(range(-160, 151, 20)) 
            
            if set(x_positions) >= set(expected_positions):
                lines_to_clear.append(y)
        
        for y in sorted(lines_to_clear, reverse=True):
            self.clear_line(y)
        
        if lines_to_clear:
            self.drop_all_blocks(sorted(lines_to_clear, reverse=True))

    def clear_line(self, y_to_clear):
        self.ground = [pos for pos in self.ground if not (isinstance(pos, tuple) and pos[1] == y_to_clear)]
        
        blocks_to_remove = []
        for block in self.blocks:
            if block.ycor() == y_to_clear:
                block.hideturtle()
                blocks_to_remove.append(block)
        
        for block in blocks_to_remove:
            self.blocks.remove(block)

    def drop_all_blocks(self, cleared_lines):
        for block in self.blocks:
            drop_amount = 0
            for cleared_y in cleared_lines:
                if block.ycor() > cleared_y:
                    drop_amount += 20
            
            if drop_amount > 0:
                new_y = block.ycor() - drop_amount
                block.goto(block.xcor(), new_y)
        
        updated_ground = []
        for pos in self.ground:
            if isinstance(pos, tuple):
                x, y = pos
                drop_amount = 0
                for cleared_y in cleared_lines:
                    if y > cleared_y:
                        drop_amount += 20
                
                if drop_amount > 0:
                    updated_ground.append((x, y - drop_amount))
                else:
                    updated_ground.append(pos)
            else:
                updated_ground.append(pos)
        
        self.ground = updated_ground
    