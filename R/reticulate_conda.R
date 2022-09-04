
# reticulate uses MINIconda and not conda
# e.g. to remove _conda_ env => conda deactivate && conda remove --name solana_py --all
# e.g. to remove MINIconda => conda_remove(envname = 'solana_py', conda = "auto")
rstudioapi::restartSession()
Sys.sleep(1)


library(tidyverse)
library(reticulate)
# https://rstudio.github.io/reticulate/reference/conda-tools.html
# conda info --envs
(envs <- conda_list(conda = "auto") %>% tibble())
envname <- "solana_py"
tmp <- glue::glue('{envname} not in conda env list')
(envname %in% envs$name) %>% 
  stopifnot(tmp = .)

# conda_remove(envname = envname, conda = "auto")
# /Users/jbg/Library/r-miniconda/envs/solana_py/bin/python
# NOT (conda) /usr/local/Caskroom/miniforge/base/envs/ipi_env
# conda create --name ipi_env
# conda_create(envname = envname)

(envs2 <- conda_list(conda = "auto") %>% tibble())
# https://rstudio.github.io/reticulate/articles/versions.html
# Sys.getenv('RETICULATE_PYTHON')
# use_python()	Specify the path a specific Python binary.
# use_virtualenv()	Specify the directory containing a Python virtualenv.
# use_condaenv()	Specify the name of a Conda environment
# conda activate /Users/jbg/Library/r-miniconda/envs/solana_py
# pip install PyPortfolioOpt
use_condaenv(envname)

# https://github.com/gitbolt/solathon
(packagess = c('asyncio', 'asyncstdlib', 
  # https://www.quicknode.com/docs/solana
  'solana', 'cachetools', 'jsonrpcclient', 'requests',
  'solathon', 'fastapi', 
  'uvicorn', 
  'pyfolio', "PyPortfolioOpt", # import pypfopt
  "yfinance",
  'pandas', 'pandas-datareader', 
  'tabulate', 
  'jupyter',
  'matplotlib', 'seaborn')
)
conda_install(envname, packagess, pip = TRUE)



# import SciPy (it will be automatically discovered in "r-reticulate")
(jsonrpcclient <- import("jsonrpcclient"))
(cachetools <- import("cachetools"))
(jupyter <- import("jupyter"))
(pyfolio <- import("pyfolio"))
(seaborn <- import("seaborn"))
(tabulate <- import("tabulate"))
(pypfopt <- import("pypfopt"))
# (pyportfolioopt <- import("pyportfolioopt"))
# (PyPortfolioOpt <- import("PyPortfolioOpt"))

(asyncio <- import("asyncio"))
(asyncstdlib <- import("asyncstdlib"))
(solana <- import("solana"))
(solathon <- import("solathon"))
(fastapi <- import("fastapi"))
(pandas_datareader <- import("pandas_datareader"))
(yfinance <- import("yfinance"))



repl_python()
# import asyncio ; import asyncstdlib ; import solana ; import pandas-datareader



(py_path <- conda_python(envname = envname, 
  conda = "auto", all = TRUE)) # all Boolean; report all instances of Python found?
envs2 %>% 
  filter(name == envname) %>% 
  pull(python) ->
  py_path2
(py_path2 == py_path) %>% 
  stopifnot('path must be identical' = .)



