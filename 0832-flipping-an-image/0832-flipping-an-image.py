class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = len(image)
        if length == 1:
            return [[0]] if image[0][0] == 1 else [[1]]
        for x in range(length):
            for y in range(length//2):

                image[x][y], image[x][length-1-y] = image[x][length-1-y], image[x][y]
                if image[x][y] == 0:
                    image[x][y] = 1
                else:
                    image[x][y] = 0

                if image[x][length-1-y] == 0:
                    image[x][length-1-y] = 1
                else:
                    image[x][length-1-y] = 0
            if length%2 != 0:
                    if image[x][length//2] == 0:
                        image[x][length//2] = 1
                    else:
                        image[x][length//2] = 0
        return image

        