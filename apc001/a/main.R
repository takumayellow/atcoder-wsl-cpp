con <- file("stdin", "r")
v <- scan(con, what = numeric(), quiet = TRUE)
close(con)
x <- v[1]
y <- v[2]

# X が Y の倍数なら X の倍数はすべて Y の倍数になる。そうでなければ X 自身が答え
if (x %% y == 0) {
  cat(-1, "\n", sep = "")
} else {
  cat(format(x, scientific = FALSE), "\n", sep = "")
}
