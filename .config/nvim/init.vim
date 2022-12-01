" Plugins
call plug#begin()
"
" vim-plug
Plug 'vim-scripts/grep.vim'
Plug 'jiangmiao/auto-pairs'
Plug 'mhinz/vim-signify'
Plug 'sheerun/vim-polyglot'
Plug 'itchyny/lightline.vim'
Plug 'nvim-lua/plenary.nvim'
Plug 'norcalli/nvim-colorizer.lua'

" NerdTree
Plug 'preservim/nerdtree'
Plug 'ryanoasis/vim-devicons'

" Basic setup
set termguicolors
set number
set splitbelow

let g:lightline = {
			\ 'colorscheme': 'one',
			\ }
" Start NERDTree and put the cursor back in the other window.
" autocmd VimEnter * NERDTree | wincmd p
let NERDTreeWinSize=20
let NERDTreeMinimaUI=2
let NERDTreeDirArrows=2
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <C-s> :sp+term<CR>

call plug#end()

" Colorizer setup
lua require'plug-colorizer'
