# tree2vim
I have always loved the tree command. What if I could browse my directories visually in the terminal? But better than browsing directories is opening files in Vim and viewing inside archives. This what this simple python program is doing.

## Quick start
```bash
git clone git@github.com:mthpvg/tree2vim.git
cd tree2vim
python tree2vim.py
```

## Preview
![Preview](/images/tree2vim.gif)

## Use from anywhere (Ubuntu 14.04 LTS)
```bash
cd && mkdir .mthpvg && cd .mthpvg
git clone git@github.com:mthpvg/tree2vim.git
echo "alias tree2vim='python ~/.mthpvg/tree2vim/tree2vim.py'" >> ~/.bashrc
source ~/.bashrc
tree2vim
```