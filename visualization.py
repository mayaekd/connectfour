import numpy as np
from mayavi import mlab

CIRCLE_WIDTH = 1.5
BORDER_WIDTH = 0.2
THICKNESS = 0.5
FINENESS = 2
BOARD_WIDTH = 7
BOARD_HEIGHT = 6


# Setting up values to draw the "board"

t = np.linspace(0,8,FINENESS*8+1)
xCircle = CIRCLE_WIDTH * np.cos(t*np.pi/4)
zCircle = CIRCLE_WIDTH * np.sin(t*np.pi/4)

halfSquareLength = CIRCLE_WIDTH + BORDER_WIDTH

xSquare = np.concatenate((
			halfSquareLength*np.ones((1,FINENESS)),
			np.linspace(halfSquareLength,-halfSquareLength,FINENESS*2+1),
			-halfSquareLength*np.ones((1,FINENESS*2-1)),
			np.linspace(-halfSquareLength,halfSquareLength,FINENESS*2+1),
			halfSquareLength*np.ones((1,FINENESS))
			), axis = None)


zSquare = np.concatenate((
			np.linspace(0,halfSquareLength,FINENESS+1),
			halfSquareLength*np.ones((1,FINENESS*2-1)),
			np.linspace(halfSquareLength,-halfSquareLength,FINENESS*2+1),
			-halfSquareLength*np.ones((1,FINENESS*2-1)),
			np.linspace(-halfSquareLength,0,FINENESS+1),
			), axis = None)

yBack = 0*t
yFront = THICKNESS + yBack


x = np.vstack((xCircle,xSquare,xSquare,xCircle))
y = np.vstack((yFront,yFront,yBack,yBack))
z = np.vstack((zCircle,zSquare,zSquare,zCircle))

squareLength = 2 * halfSquareLength

# Drawing the board
for i in range(BOARD_WIDTH):
	for j in range(BOARD_HEIGHT):
		mlab.mesh(x+i*squareLength,y,z+j*squareLength,color = (245/256, 233/256, 66/256))


# Setting up values to draw the token
xToken = np.vstack((0*t,xCircle,xCircle,0*t))
yToken = np.vstack((0.9*yFront,0.9*yFront,0.1*yFront,0.1*yFront))
zToken = np.vstack((0*t,zCircle,zCircle,0*t))


# Animating the token falling
@mlab.animate(delay = 1000)
def play_piece(column, smoothness = 10):
	token = mlab.mesh(xToken+(squareLength*column),yToken,zToken+(BOARD_HEIGHT*squareLength*1.2), color = (1,0,0))
	for i in range(smoothness):
		token.mlab_source.reset(x = xToken+(squareLength*column),y = yToken, z = zToken+(BOARD_HEIGHT*squareLength*1.2)*(smoothness - i - 1)/smoothness , color = (1,0,0))
		yield

if __name__ == "__main__":
	play_piece(3)
	mlab.show()


