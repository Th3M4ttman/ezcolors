
from .Colors import *
import os

def color_to_terminal(col: Color):
	if type(col) == int:
		return col
	colors = (Black,Red, Green, Yellow, Blue, Purple, Cyan, Grey, LRed, LGreen, LYellow, LBlue, LPurple, LCyan, White)
	closest = col.closest(colors=colors)
	for i, color in enumerate(colors):
		if closest == color:
			return i
			
def terminal_to_color(col: int):
	colors = (Black,Red, Green, Yellow, Blue, Purple, Cyan, Grey, LRed, LGreen, LYellow, LBlue, LPurple, LCyan, White)
	
	if type(col) == Color:
		return col
	else: return colors[col]

def splash(globalsref, color = White, title = None, sub = "---", author = None, version = None, lines=True, doc=True, use_mptc=None, bg = None, bg2 = None, edge = 14, text_bg = None, text_fg = None, pulse = True, pulse_edge = False):
		if title is None:
			title = globalsref["__file__"].split("/")[-1]
		if "__title__" in globalsref.keys():
				title = globalsref["__title__"]
		if "__subtitle__" in globalsref.keys():
				sub = globalsref["__subtitle__"]
		if author is None:
			if "__author__" in globalsref.keys():
				author = globalsref["__author__"]
			else:
				author = "Me"
		if version is None:
			if "__version__" in globalsref.keys():
				version  = globalsref["__version__"]
			else:
				version = "0.0.1"
		if "__doc__" in globalsref.keys() and  doc in (True, None):
			doc = globalsref["__doc__"]
			
		if doc is True:
			doc = False
				
		mptc_enabled = False
		try:
			import mptc
			mptc_enabled = True
		except:
			pass
		
		#print("mptc", cBool(mptc_enabled))
		
		x, y = os.popen('stty size', 'r').read().split()
		y = int(y)
		
		if mptc_enabled and (use_mptc is True or use_mptc is None):
			if bg is None:
				bg = LRed
			if bg2 is None:
				bg2 = Red
			if edge is None:
				edge = White
			
			bg = color_to_terminal(bg)
			bg2 = color_to_terminal(bg2)
			edge = color_to_terminal(edge)
			
			if text_fg is None:
				text_fg = 14
			else:
				text_fg = color_to_terminal(text_fg)
			if text_bg is None:
				text_bg = bg2
			else:
				text_bg = color_to_terminal(text_bg)
				
			
			print(mptc.Splash(title=title, pulse=pulse, bg=bg, bg2=bg2, edges=edge, textbg=text_bg, textfg=text_fg, auth=f"By {author}", sub=sub))
			if doc:
				print()
				print(doc)
				print()
				print(mptc.seperator(length=y, colour=edge, ld=pulse_edge))
			print()
			return
			
		color = terminal_to_color(color)
		if bg2 is not None:
			color = terminal_to_color(bg2)
		if  bg is not None:
			color = terminal_to_color(bg)
		if  text_fg is not None:
			color = terminal_to_color(text_fg)
		if lines:
			print("="*y)
			print("|"+(" "*(y-2))+"|")
			print("|"+color.text(f"{title}".center(y-2)) + "|")
			print("|"+f"{color.text(sub).center(y+7)}"+"|")
			print("|"+color.text(f"By {author}".center(y-2))+"|")
			print("|"+color.text(f"{version}".center(y-2))+"|")
			print("|"+(" "*(y-2))+"|")
			print("="*y)
			print()
		else:
			print()
			print(color.text(f"{title}".center(y)))
			print(color.text(sub))
			print(color.text(f"By {author}".center(y)))
			print(color.text(f"{version}".center(y)))
			print()
			print()
		
		
		if doc:
			print(doc)
			print()
			if lines:
				print("="*y)
			print()

#splash()