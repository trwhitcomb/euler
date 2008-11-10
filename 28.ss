; Project Euler
; Problem 28
; Spiral Sums - given a 5x5 spiral matrix
;  21 22 23 24 25
;  20  7  8  9 10
;  19  6  1  2 11
;  18  5  4  3 12
;  17 16 15 14 13
; the sum of both diagonals is 101.  What is the sum of both
; diagonals in a 1001x1001 spiral formed the same way?

; Define the spiral level k as the extent of the spiral - for 
; the 5x5 matrix above, k=2 (since we assume that a 1x1
; matrix has spiral level zero).  This means that the corner 
; elements are given by
; corner(k) = (2k + 1)^2 - (0 2k 4k 6k)
; Note that the difference between the corners is 2k.

; Find the sum of the diagonals of a spiral matrix with spiral level k
(define (diag-sum k)
  (if (= 0 k)
      1
      (+ (corner-sum k)
         (diag-sum (- k 1)))))

; Note that the only elements that one needs to compute are 2 of
; the 4 corners.  Since the upper-right corner is (2k+1)^2, use
; that and the lower-left corner.
(define (corner-sum k)
  (define (square x)
    (* x x))
  (define corner-spacing
    (* 2 k))
  (define upper-right-corner-value
    (square (+ (* 2 k) 1)))
  (define upper-left-corner-value
    (- upper-right-corner-value corner-spacing))
  (define lower-left-corner-value
    (- upper-left-corner-value corner-spacing))
  (define lower-right-corner-value
    (- lower-left-corner-value corner-spacing))
  (+ upper-right-corner-value
     upper-left-corner-value
     lower-left-corner-value
     lower-right-corner-value))

; Another way to call this - just provide the dimension of the matrix
; (either the # of rows or the # of columns) - note that n is always odd
(define (spiral-sum n)
  (diag-sum (/ (- n 1) 2)))

(spiral-sum 1001)



