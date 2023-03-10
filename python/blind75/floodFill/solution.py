class Solution:
    ## The problem of this approach is: when old_color and new_color is the same, it will fall 
    # into infinite loop !!
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def flood(image: list[list[int]], sr: int, sc: int, new_color: int, old_color):
            r_cnt, c_cnt = len(image), len(image[0])

            if sr < 0 or sr >= r_cnt or sc < 0 or sc >= c_cnt or image[sr][sc] != old_color:
                return 
            else:
                image[sr][sc] = new_color
                flood(image, sr+1, sc, new_color, old_color)
                flood(image, sr, sc+1, new_color, old_color)
                flood(image, sr-1, sc, new_color, old_color)
                flood(image, sr, sc-1, new_color, old_color)

        old_color = image[sr][sc]
        flood(image, sr, sc, color, old_color)
        return image
        
    def floodFill2(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old_color = image[sr][sc]
        new_color = color

        def flood(image: list[list[int]], sr: int, sc: int):
            r_cnt, c_cnt = len(image), len(image[0])

            # Avoid infinite loop if the new and old colors (image[sr][sc] == new_color) are the same...
            if sr < 0 or sr >= r_cnt or sc < 0 or sc >= c_cnt or image[sr][sc] == new_color:
                return 

            if image[sr][sc] == old_color:
                image[sr][sc] = new_color
                flood(image, sr+1, sc)
                flood(image, sr, sc+1)
                flood(image, sr-1, sc)
                flood(image, sr, sc-1)

        flood(image, sr, sc)
        return image
        

        

    
    