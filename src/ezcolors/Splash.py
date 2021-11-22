
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
		if title is None and "__file__" in globalsref.keys():
			title = globalsref["__file__"].split("/")[-1]
		else:
			title = "Unnamed"
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
		
		
		if "__colors__" in globalsref.keys():
			colors = globalsref["__colors__"]
			if type(colors) in (list, tuple):
				if len(colors) == 3:
					edge = colors[3]
				colors = list(colors)
				while len(colors) < 2:
					colors.append(colors[0])
			elif type(colors) == str:
				colors = [Color(colors), Color(colors), Color(colors)]
			elif type(colors) == int or isinstance(colors, Color):
				colors = [colors]
				while len(colors) < 2:
					colors.append(colors[0])
			bg = colors[0]
			bg2 = colors[1]
			color = colors[0]
		
		if "__textcolors__" in globalsref.keys():
			colors = globalsref["__textcolors__"]
			if type(colors) in (list, tuple):
				colors = list(colors)
				while len(colors) < 2:
					colors.append(bg)
			elif type(colors) == str:
				colors = [Color(colors), bg]
			elif type(colors) == int or isinstance(colors, Color):
				colors = [colors]
				while len(colors) < 2:
					colors.append(bg)
					
			text_fg = colors[0]
			text_bg = colors[1]
		
			
		if doc is True:
			doc = False
				
		mptc_enabled = False
		try:
			import mptc
			mptc_enabled = True
		except:
			pass
		
		#print("mptc", cBool(mptc_enabled))
		try:
			x, y = os.popen('stty size', 'r').read().split()
		except:
			x, y = 48, 60
		tx, ty = x, y
		
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
				
			
			print(mptc.Splash(title=title, pulse=pulse, bg=bg, bg2=bg2, edges=edge, textbg=text_bg, textfg=text_fg, auth=f"By {author}", sub=sub, ver=version))
			if doc:
				print()
				print(str(doc).center(ty))
				print()
				print(mptc.seperator(length=ty, colour=edge, ld=pulse_edge))
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
			print("="*ty)
			print("|"+(" "*(ty-2))+"|")
			print("|"+color.text(f"{title}".center(ty-2)) + "|")
			print("|"+f"{color.text(sub).center(y+7)}"+"|")
			print("|"+color.text(f"By {author}".center(ty-2))+"|")
			print("|"+color.text(f"{version}".center(ty-2))+"|")
			print("|"+(" "*(ty-2))+"|")
			print("="*ty)
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
			print(str(doc).center(ty))
			print()
			if lines:
				print("="*ty)
			print()

#splash()