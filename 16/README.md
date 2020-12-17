# Day 16

## Performance
Part A
```bash
(advent2020) ➜  16 git:(master) ✗ time python3 16a.py 
part a: 32842
python3 16a.py  0.08s user 0.01s system 99% cpu 0.092 total
```

Part B
```bash
(advent2020) ➜  16 git:(master) ✗ time python3 16b.py
pos | values for that position
000 |  067 082 082 096 102 102 103 105 108 118 119 119 120 120 127 131 136 142 146 148 157 170 170 170 171 172 180 208 216 216 218 219 221 223 224 228 228 231 244 250 254 257 257 258 260 261 261 262 263 267 275 278 280 282 289 291 304 310 310 311 316 317 317 319 321 325 327 328 350 352 356 365 382 387 387 391 395 395 397 402 403 404 412 414 416 417 418 419 420 421 422 429 429 432 436 440 445 445 449 463 466 475 480 503 513 520 520 523 536 550 550 552 554 555 569 587 588 602 603 608 615 618 619 621 630 643 645 646 647 649 651 681 683 684 685 687 688 689 690 691 710 721 721 724 726 726 728 728 729 733 743 749 753 755 756 762 763 778 781 784 784 787 790 798 800 810 814 826 834 838 844 844 845 850 855 862 863 868 873 873 876 877 879 883 896 904 914 921 928 930 946 
001 |  052 059 074 074 080 080 089 090 092 094 098 101 106 108 111 111 117 130 131 138 150 150 152 154 156 157 158 159 161 163 194 195 198 214 216 223 225 225 230 231 232 232 247 258 259 263 263 274 276 279 280 288 289 289 293 295 296 296 296 302 303 303 305 307 308 317 317 319 322 323 323 326 334 337 338 339 343 349 349 352 354 354 381 384 385 389 398 398 398 401 408 415 417 426 427 430 430 431 435 445 446 447 455 461 465 465 467 472 475 528 528 551 562 599 601 605 609 610 614 614 615 616 617 618 622 622 629 631 632 635 637 639 643 650 682 683 684 686 692 724 730 739 741 744 754 755 760 761 762 762 765 770 771 775 778 779 789 792 792 811 817 825 825 826 838 839 839 863 863 866 875 878 881 883 889 904 905 906 912 916 916 917 924 926 927 942 945 947 947 948 949 
002 |  056 056 056 058 064 065 066 074 074 081 084 084 089 095 097 106 109 114 115 115 116 120 121 123 125 128 132 136 145 151 155 159 163 165 169 169 170 184 201 228 230 230 232 232 234 243 257 257 261 263 266 268 271 274 279 283 286 288 296 299 302 309 312 318 319 320 323 328 330 336 337 337 338 342 346 346 351 367 381 384 387 392 402 404 406 413 417 420 420 421 426 431 431 435 444 453 454 462 468 470 471 471 477 498 507 514 525 527 549 551 553 568 587 591 597 597 601 604 609 615 626 631 633 639 646 649 649 677 683 684 689 701 716 717 719 723 724 739 740 744 746 758 765 766 769 770 774 780 784 787 787 788 788 789 792 795 802 814 816 817 819 825 828 833 839 840 844 850 850 853 870 874 879 882 887 891 893 894 898 904 907 911 911 912 912 916 920 937 947 948 949 
003 |  054 066 076 079 080 084 086 091 091 096 096 098 101 104 108 108 114 120 123 130 132 137 141 141 145 148 149 149 153 156 158 159 162 162 163 163 164 172 173 205 210 212 213 216 217 218 224 231 249 254 256 265 266 268 269 270 272 273 284 285 286 291 291 294 303 304 305 305 307 307 308 317 319 321 324 326 332 344 348 370 381 382 386 391 392 395 396 397 399 400 400 401 401 401 402 406 409 409 413 419 422 429 431 435 437 453 459 463 470 475 511 513 517 520 528 553 556 558 558 559 559 560 562 584 592 595 597 599 603 603 615 619 629 634 643 644 676 676 680 716 717 720 722 724 728 733 736 740 742 745 752 755 760 763 770 771 773 775 778 783 784 793 793 820 820 831 839 840 842 844 848 849 864 864 872 872 873 877 879 882 888 889 895 902 908 909 912 913 917 921 924 
004 |  050 053 055 058 063 063 077 079 083 086 090 097 101 105 107 112 138 141 141 142 146 149 150 155 155 165 166 166 169 169 170 196 198 207 214 216 219 220 220 257 264 266 267 268 271 272 277 278 279 285 288 290 291 293 298 302 302 308 312 323 326 340 343 351 351 352 354 366 382 382 383 390 391 403 406 408 409 415 418 423 424 427 431 432 446 446 451 452 452 459 460 462 466 466 466 467 471 471 474 475 484 491 491 498 510 510 516 522 528 559 561 562 562 569 589 589 589 592 596 604 605 612 614 618 620 624 628 629 633 640 642 649 675 676 676 677 678 682 685 704 716 724 724 752 752 754 758 758 767 767 768 769 771 789 793 806 811 812 813 815 820 823 824 825 826 831 838 840 840 844 847 848 867 869 871 873 874 876 878 886 888 890 915 919 922 929 937 941 948 948 948 
005 |  050 052 057 063 066 079 083 088 101 108 115 118 131 138 145 145 147 148 151 156 162 162 169 172 172 176 193 202 211 212 212 213 224 231 232 233 233 235 243 247 248 251 264 265 274 279 290 294 295 297 303 303 305 310 318 324 325 329 330 332 332 333 334 348 362 381 383 389 392 393 394 397 398 401 402 403 405 406 406 409 412 413 415 424 428 436 437 438 443 452 455 460 472 473 485 500 507 509 512 516 519 521 554 556 558 560 562 578 587 592 597 605 606 610 614 625 628 630 631 635 636 643 645 645 649 678 678 679 683 683 684 690 691 703 715 716 718 724 726 728 730 731 735 737 743 744 754 755 763 773 774 775 778 784 797 806 811 814 818 821 823 827 837 844 860 862 863 864 866 872 873 874 876 880 880 885 885 889 890 892 898 903 904 907 912 919 921 925 928 928 933 
006 |  055 059 060 061 065 075 077 090 092 093 097 101 107 107 113 117 117 120 122 125 125 128 134 144 145 152 153 156 159 159 161 164 168 171 171 210 214 215 217 219 228 228 232 233 247 252 253 255 259 260 261 263 273 275 281 286 292 294 297 300 301 303 305 306 309 317 319 320 322 325 327 333 343 344 347 349 351 352 366 382 387 391 392 393 395 397 401 401 406 406 411 414 420 423 423 424 428 430 432 436 439 439 449 453 457 459 463 508 511 513 520 527 551 555 559 562 567 589 591 593 599 599 611 626 626 627 631 631 633 635 639 641 642 645 649 650 677 680 690 691 720 721 725 728 730 730 736 737 743 757 759 768 772 775 784 790 811 813 817 817 818 823 826 839 850 867 868 869 872 877 881 884 886 888 892 893 894 895 906 906 907 909 913 914 915 916 920 925 928 941 947 
007 |  050 055 060 078 089 089 097 107 109 110 113 115 117 120 123 128 129 133 138 141 144 147 148 149 150 156 158 207 210 214 214 216 230 233 248 253 253 255 256 267 274 276 277 278 283 285 286 286 288 292 305 305 312 319 323 332 335 336 337 337 338 340 350 351 353 358 376 388 393 394 396 404 406 411 412 423 426 429 434 438 440 442 462 468 473 474 484 491 491 501 512 513 514 523 551 552 553 557 559 566 589 589 589 590 593 604 606 612 613 615 615 615 617 620 621 629 636 636 637 643 644 645 646 651 677 684 690 691 716 722 723 727 729 730 731 735 752 756 757 759 761 762 766 768 770 782 783 786 790 808 811 812 813 814 817 821 824 826 826 826 828 833 842 845 850 850 864 867 868 868 869 872 874 876 879 881 883 884 885 886 887 893 906 906 910 912 915 915 924 933 946 
008 |  050 052 053 055 055 056 056 060 075 077 078 079 088 091 091 092 097 103 104 104 107 108 109 112 112 115 122 136 148 149 157 160 160 161 162 163 171 173 175 193 195 203 210 211 211 229 237 252 253 255 265 266 285 287 291 297 297 298 303 306 315 324 325 326 331 334 336 337 338 341 349 349 353 354 356 361 384 388 388 388 390 394 403 405 406 409 411 417 420 427 430 434 435 436 436 449 457 459 478 501 515 518 520 522 550 550 551 553 554 554 558 584 600 610 611 620 622 625 627 633 633 639 641 645 648 649 650 679 686 686 692 704 720 722 724 725 728 729 731 740 741 754 754 761 763 763 764 769 769 770 773 780 783 785 786 787 792 800 806 819 820 824 828 832 838 840 848 854 864 864 868 870 871 876 893 894 901 904 905 906 908 908 911 919 922 924 925 925 927 938 949 
009 |  058 059 060 075 078 085 086 092 100 101 103 105 113 120 121 122 123 130 136 148 148 151 154 160 163 164 164 166 203 210 210 211 212 214 221 226 227 245 247 248 251 257 262 263 272 276 277 291 305 308 317 320 325 326 326 332 336 336 336 340 343 352 376 385 387 396 397 398 403 404 409 412 417 420 421 426 437 442 444 446 446 447 450 453 454 464 466 466 469 483 492 501 509 512 513 514 521 551 555 572 592 594 595 604 606 607 613 614 615 621 621 628 632 639 640 640 643 645 646 650 680 680 681 682 684 684 684 704 718 719 722 731 731 734 734 754 759 760 761 775 784 790 792 802 813 820 827 828 833 841 843 846 847 865 866 869 869 871 871 875 877 880 883 883 883 890 891 893 893 894 895 902 904 904 905 906 908 908 909 916 918 920 922 925 926 926 929 929 938 941 942 
010 |  050 062 063 074 076 078 078 082 089 091 097 101 104 105 107 108 115 115 116 116 119 120 121 125 127 133 134 141 144 145 147 148 150 151 158 159 159 163 164 165 167 173 194 196 210 210 210 215 234 235 235 247 258 268 274 277 288 294 297 297 301 302 305 311 319 323 327 332 340 341 342 345 384 386 387 388 389 389 393 394 414 414 424 433 433 434 436 436 441 443 454 459 465 466 467 468 471 471 472 473 474 475 475 507 509 509 513 515 516 516 549 550 553 558 561 572 587 593 596 598 600 612 616 635 635 641 647 676 678 680 682 683 684 688 689 715 718 725 731 734 739 740 742 742 753 755 757 766 768 774 776 781 782 785 789 790 790 791 793 812 815 815 816 818 819 838 839 867 871 877 878 879 888 893 894 905 908 910 916 916 917 917 919 920 920 929 942 944 947 948 948 
011 |  051 053 060 065 066 075 084 086 093 093 094 106 108 108 110 116 118 120 122 124 125 138 142 142 146 161 167 173 187 200 213 221 221 228 228 232 234 238 247 254 255 267 269 272 277 285 286 288 302 313 314 320 324 324 324 329 329 332 335 336 339 341 344 344 350 374 382 388 389 399 400 401 402 403 403 403 406 411 420 424 428 432 438 440 445 463 465 472 478 499 512 515 518 519 519 520 524 547 550 552 554 556 556 557 558 565 588 589 594 596 599 602 605 613 616 618 619 623 631 632 632 638 638 650 650 675 676 677 683 684 692 692 695 718 721 723 729 731 735 740 745 748 759 763 766 772 787 792 792 793 799 801 805 813 816 817 818 824 827 835 838 839 840 840 844 845 845 846 847 859 868 868 871 877 883 891 893 901 903 905 911 913 914 915 921 924 927 930 941 944 945 
012 |  057 061 076 078 081 084 085 100 102 108 111 112 114 114 115 123 127 127 129 131 134 141 143 145 154 155 159 196 197 207 211 212 213 219 220 220 225 228 234 235 248 250 255 257 257 257 258 259 282 288 288 289 291 292 297 298 302 305 318 320 321 321 322 327 335 335 336 341 343 347 352 352 352 355 371 382 387 388 396 398 404 411 418 423 425 429 430 433 435 437 442 445 447 453 454 457 457 463 465 467 472 474 482 491 511 527 549 555 560 577 595 599 600 607 610 632 632 634 641 641 643 644 646 648 649 679 681 682 684 686 715 716 717 720 723 731 738 757 759 760 761 769 775 775 775 779 782 785 786 787 790 790 792 793 793 793 802 811 816 817 818 819 821 822 825 826 827 829 839 848 849 850 850 862 863 865 866 867 868 871 871 872 877 877 882 887 909 918 925 942 949 
013 |  052 055 057 058 059 064 066 076 076 081 087 088 090 096 097 101 101 106 107 111 112 112 118 127 131 131 135 145 146 148 150 152 154 157 157 161 165 166 170 173 203 214 215 216 218 218 225 227 234 248 249 256 256 258 262 270 274 276 276 277 280 281 282 283 284 285 295 297 297 297 302 307 315 317 319 320 321 323 324 330 331 334 335 346 349 353 354 380 383 394 398 399 399 402 408 408 411 414 415 419 424 433 434 438 443 448 449 460 463 465 488 491 508 514 514 516 516 518 519 520 520 555 556 557 557 569 592 593 596 602 605 611 613 614 619 620 624 625 634 634 637 651 677 682 682 686 691 716 717 718 719 722 730 744 754 762 763 764 767 770 770 772 776 780 781 788 789 815 823 832 843 847 847 849 863 866 869 875 877 879 887 892 903 914 914 917 918 921 928 945 948 
014 |  050 056 061 077 077 078 079 080 081 091 092 099 099 104 113 114 115 116 124 127 129 130 131 151 153 153 154 155 160 161 168 170 171 194 195 195 197 198 214 215 216 218 221 225 225 226 227 229 247 249 255 256 257 260 266 269 272 273 274 274 281 282 285 285 288 301 304 304 304 304 314 315 315 325 327 330 330 330 332 337 340 341 347 354 355 382 382 389 393 397 410 410 418 421 425 435 435 436 438 446 454 457 461 466 467 492 512 515 528 549 553 553 556 558 559 560 562 562 588 588 595 596 599 600 608 610 611 614 618 620 621 631 636 639 642 643 646 647 679 680 718 719 723 734 736 737 742 743 754 755 756 758 759 761 772 779 779 779 780 781 781 782 785 800 801 812 812 818 821 826 828 840 843 862 866 866 866 873 880 892 905 906 907 909 909 925 928 928 941 942 943 
015 |  050 051 057 057 059 060 063 077 077 078 083 091 099 100 102 103 103 106 114 117 118 123 126 127 130 131 132 133 140 143 144 144 145 165 170 193 210 210 213 213 214 214 220 222 222 226 232 233 234 249 250 251 251 252 252 252 258 262 263 263 264 268 270 277 284 285 287 288 295 297 313 315 316 327 335 338 347 352 372 385 389 396 398 398 400 408 411 412 419 422 424 429 431 439 446 452 455 457 457 462 462 462 464 467 468 472 515 517 551 557 581 594 597 603 605 605 606 608 612 620 625 628 630 631 631 632 635 635 642 643 645 649 675 675 678 683 684 689 690 691 717 718 720 723 725 729 734 735 744 753 754 754 756 759 761 761 764 771 773 776 778 811 824 827 836 840 842 842 844 866 871 874 876 880 881 885 890 892 902 907 907 914 914 916 916 919 919 920 944 946 947 
016 |  055 060 075 082 084 087 087 090 090 091 101 107 113 118 128 132 132 132 135 142 145 145 149 162 162 171 198 203 211 211 214 220 221 223 225 232 232 234 235 249 255 256 256 271 271 279 286 288 291 295 295 300 301 305 305 308 309 314 318 319 327 334 336 337 339 340 340 342 352 352 354 357 357 379 385 392 397 400 401 409 411 415 416 417 419 422 436 442 447 452 453 463 465 470 474 481 494 507 508 509 510 515 515 516 516 520 520 527 527 551 579 587 588 590 594 596 597 599 603 604 607 607 610 614 618 621 622 623 623 630 631 633 640 640 640 651 678 687 719 727 730 730 730 731 731 736 740 742 745 745 758 774 774 778 780 781 784 793 810 811 813 820 821 821 834 846 848 850 864 872 873 873 874 879 891 892 893 894 894 904 909 912 916 917 917 922 922 923 937 948 949 
017 |  050 051 052 059 060 062 062 065 065 075 076 082 086 087 091 094 095 098 103 105 107 107 109 109 117 121 124 125 126 129 132 132 139 151 153 154 155 159 163 163 165 166 167 173 173 173 188 194 198 198 198 204 221 225 227 228 234 235 246 256 257 266 266 270 270 271 292 298 299 300 307 308 310 313 316 317 329 331 340 347 355 370 385 398 402 403 407 409 422 427 436 440 443 443 451 452 456 457 470 470 474 488 492 504 511 513 515 516 520 522 528 528 553 555 555 566 605 609 610 612 615 626 627 643 647 649 683 684 684 684 685 705 715 720 720 722 724 724 730 731 731 732 734 745 756 760 762 763 764 767 774 774 775 784 784 784 786 786 787 788 802 813 825 826 830 839 840 846 847 850 870 876 877 877 882 891 893 893 907 920 922 922 930 941 942 945 946 947 947 947 948 
018 |  060 065 065 083 084 084 086 088 089 090 093 093 104 114 114 117 125 129 133 140 142 142 142 147 149 150 150 152 155 164 167 174 202 215 217 233 240 254 257 257 262 262 267 272 281 285 286 288 302 302 310 317 317 321 328 339 343 344 347 349 350 352 356 370 382 386 388 389 390 391 395 399 400 402 404 409 411 415 415 417 417 421 422 431 433 434 439 441 446 448 449 449 451 457 458 462 470 471 471 480 505 507 514 521 551 553 553 556 560 575 592 597 603 610 613 623 633 635 639 644 647 675 687 690 714 716 716 717 717 719 725 726 738 739 741 752 752 757 760 763 767 770 772 774 774 775 779 783 784 785 789 801 808 811 814 819 821 822 825 826 826 829 839 840 840 848 849 850 862 864 871 872 875 876 877 880 880 882 885 886 887 893 899 903 905 910 910 912 932 941 948 
019 |  051 055 061 075 077 081 082 083 087 091 106 106 113 114 117 122 129 130 130 131 132 135 142 147 147 152 160 164 197 205 217 217 218 221 223 224 228 232 249 249 249 251 254 258 259 260 261 264 265 267 274 282 285 288 288 294 299 300 300 302 305 311 315 319 321 324 326 328 329 330 330 331 332 335 336 336 337 343 345 346 348 349 358 359 382 390 394 396 406 407 412 415 422 422 432 435 436 436 437 445 452 459 460 461 461 485 492 492 511 516 517 517 518 551 553 555 557 581 587 591 595 599 608 611 615 621 623 624 634 635 637 638 650 650 651 676 683 683 683 684 688 689 689 690 692 723 727 728 729 732 737 737 737 738 740 743 744 758 761 775 777 807 812 824 824 825 836 846 847 849 865 866 867 871 875 875 877 879 883 888 902 912 913 914 919 921 924 928 935 941 949 
Poss position per rule: {'departure location': {1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}, 'departure station': {1, 3, 4, 6, 7, 10, 12, 13, 14, 15, 16, 19}, 'departure platform': {1, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}, 'departure track': {1, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 19}, 'departure date': {1, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 19}, 'departure time': {1, 3, 6, 7, 10, 12, 13, 14, 15, 16, 19}, 'arrival location': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}, 'arrival station': {14}, 'arrival platform': {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 'arrival track': {1, 3, 6, 10, 13, 14, 15}, 'class': {1, 14}, 'duration': {1, 3, 6, 10, 12, 13, 14, 15, 16, 19}, 'price': {1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19}, 'route': {1, 3, 6, 10, 12, 13, 14, 15}, 'row': {1, 10, 6, 14}, 'seat': {1, 3, 6, 10, 14, 15}, 'train': {1, 6, 10, 14, 15}, 'type': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}, 'wagon': {1, 3, 6, 10, 12, 13, 14, 15, 19}, 'zone': {1, 10, 14}}
number of poss rules per position: Counter({14: 20, 1: 19, 10: 18, 6: 17, 15: 16, 3: 15, 13: 14, 12: 13, 19: 12, 16: 11, 7: 10, 4: 9, 9: 8, 17: 7, 18: 6, 8: 5, 5: 4, 2: 3, 11: 2, 0: 1})

Possible rules per position
000 |  arrival platform
001 |  arrival location, arrival platform, arrival track, class, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, row, seat, train, type, wagon, zone
002 |  arrival location, arrival platform, type
003 |  arrival location, arrival platform, arrival track, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, seat, type, wagon
004 |  arrival location, arrival platform, departure date, departure location, departure platform, departure station, departure track, price, type
005 |  arrival location, arrival platform, price, type
006 |  arrival location, arrival platform, arrival track, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, row, seat, train, type, wagon
007 |  arrival location, arrival platform, departure date, departure location, departure platform, departure station, departure time, departure track, price, type
008 |  arrival location, arrival platform, departure location, price, type
009 |  arrival location, arrival platform, departure date, departure location, departure platform, departure track, price, type
010 |  arrival location, arrival platform, arrival track, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, row, seat, train, type, wagon, zone
011 |  arrival platform, type
012 |  arrival location, arrival platform, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, type, wagon
013 |  arrival location, arrival platform, arrival track, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, type, wagon
014 |  arrival location, arrival platform, arrival station, arrival track, class, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, row, seat, train, type, wagon, zone
015 |  arrival location, arrival platform, arrival track, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, route, seat, train, type, wagon
016 |  arrival location, arrival platform, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, type
017 |  arrival location, arrival platform, departure date, departure location, departure platform, price, type
018 |  arrival location, arrival platform, departure location, departure platform, price, type
019 |  arrival location, arrival platform, departure date, departure location, departure platform, departure station, departure time, departure track, duration, price, type, wagon

part b: [83, 89, 109, 113, 173, 167] 2628667251989
python3 16b.py  0.09s user 0.01s system 98% cpu 0.107 total
```