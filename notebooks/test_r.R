cat("R:", R.version.string, "\n")
cat("Lib:", .libPaths()[1], "\n")
set.seed(1); cat("Sample:", paste(round(rnorm(5),3), collapse=", "), "\n")
