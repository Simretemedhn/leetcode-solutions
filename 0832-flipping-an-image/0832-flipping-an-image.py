class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = len(image)
        for x in range(length):
            image[x].reverse()
            for y in range(length):
                if image[x][y] == 0:
                    image[x][y] = 1
                else:
                    image[x][y] = 0
        return image

        