# NeonUserBot / əkmə lülüş baş
# petito bled
# ⌭ R ⲉ ⳑ ⲁ ⲏ x🇺🇸ཊཏ̶ ꪀꫀꪮꪀ ོ✞

from userbot.events import register as relahx
from userbot.cmdhelp import CmdHelp


basemojitext = [
    "a",
    "b",
    "c",
    "ç",
    "d",
    "e",
    "f",
    "g",
    "ğ",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "ö",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "ü",
    "v",
    "w",
    "x",
    "y",
    "z",
    "@",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

emojis = [
    "⁭\
    \n                    💖\
    \n                  💖💖\
    \n               💖💖💖\
    \n            💖💖 💖💖\
    \n          💖💖    💖💖\
    \n        💖💖       💖💖\
    \n      💖💖💖💖💖💖\
    \n     💖💖💖💖💖💖💖\
    \n   💖💖                 💖💖\
    \n  💖💖                    💖💖\
    \n💖💖                       💖💖\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n",
    "⁭\
    \n          💛💛💛💛💛💛\
    \n     💛💛💛💛💛💛💛💛\
    \n   💛💛                      💛💛\
    \n 💛💛\
    \n💛💛\
    \n💛💛\
    \n 💛💛\
    \n   💛💛                      💛💛\
    \n     💛💛💛💛💛💛💛💛\
    \n         💛💛💛💛💛💛\
    \n",
    "⁭\
    \n          💝💝💝💝💝💝\
    \n     💝💝💝💝💝💝💝💝\
    \n   💝💝                      💝💝\
    \n 💝💝\
    \n💝💝\
    \n💝💝\
    \n 💝💝\
    \n   💝💝                      💝💝\
    \n     💝💝💝💝💝💝💝💝\
    \n         💝💝💝💝💝💝\
    \n\
    \nㅤ               💝💝\
    \n",
    "⁭\
    \n💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙                      💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                         💙💙\
    \n💙💙                      💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙\
    \n",
    "⁭\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟\
    \n💟💟💟💟💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚\
    \n💚💚\
    \n",
    "⁭\
    \n          💜💜💜💜💜💜\
    \n     💜💜💜💜💜💜💜💜\
    \n   💜💜                     💜💜\
    \n 💜💜\
    \n💜💜                💜💜💜💜\
    \n💜💜                💜💜💜💜\
    \n 💜💜                        💜💜\
    \n   💜💜                      💜💜\
    \n     💜💜💜💜💜💜💜💜\
    \n          💜💜💜💜💜💜\
    \n",
    "\
    \nㅤ      🧡🧡🧡🧡🧡🧡\
    \n\
    \n          🧡🧡🧡🧡🧡🧡\
    \n     🧡🧡🧡🧡🧡🧡🧡🧡\
    \n   🧡🧡                     🧡🧡\
    \n 🧡🧡\
    \n🧡🧡                🧡🧡🧡🧡\
    \n🧡🧡                🧡🧡🧡🧡\
    \n 🧡🧡                        🧡🧡\
    \n   🧡🧡                      🧡🧡\
    \n     🧡🧡🧡🧡🧡🧡🧡🧡\
    \n          🧡🧡🧡🧡🧡🧡\
    \n",
    "⁭\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n💖💖                        💖💖\
    \n",
    "⁭\
    \n💗💗💗💗💗💗\
    \n💗💗💗💗💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n          💗💗\
    \n💗💗💗💗💗💗\
    \n💗💗💗💗💗💗\
    \n",
    "⁭\
    \n         💛💛💛💛💛💛\
    \n         💛💛💛💛💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n                  💛💛\
    \n💛💛          💛💛\
    \n  💛💛       💛💛\
    \n   💛💛💛💛💛\
    \n      💛💛💛💛\
    \n",
    "⁭\
    \n💙💙                  💙💙\
    \n💙💙             💙💙\
    \n💙💙        💙💙\
    \n💙💙   💙💙\
    \n💙💙💙💙\
    \n💙💙 💙💙\
    \n💙💙     💙💙\
    \n💙💙         💙💙\
    \n💙💙              💙💙\
    \n💙💙                   💙💙\
    \n",
    "⁭\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚                                    💚💚\
    \n💚💚💚                         💚💚💚\
    \n💚💚💚💚               💚💚💚💚\
    \n💚💚    💚💚       💚💚    💚💚\
    \n💚💚          💚💚💚          💚💚\
    \n💚💚               💚                💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                     💚💚\
    \n💚💚                                      💚💚\
    \n",
    "⁭\
    \n💜💜                           💜💜\
    \n💜💜💜                      💜💜\
    \n💜💜💜💜                 💜💜\
    \n💜💜  💜💜               💜💜\
    \n💜💜     💜💜            💜💜\
    \n💜💜         💜💜        💜💜\
    \n💜💜             💜💜    💜💜\
    \n💜💜                 💜💜💜💜\
    \n💜💜                       💜💜💜\
    \n💜💜                             💜💜\
    \n",
    "⁭\
    \n           💖💖💖💖💖\
    \n     💖💖💖💖💖💖💖\
    \n   💖💖                   💖💖\
    \n 💖💖                       💖💖\
    \n💖💖                         💖💖\
    \n💖💖                         💖💖\
    \n 💖💖                       💖💖\
    \n   💖💖                   💖💖\
    \n      💖💖💖💖💖💖💖\
    \n            💖💖💖💖💖\
    \n",
    "\
    \n⁭ㅤ       ❤️❤️     ❤️❤️\
    \n\
    \n           ❤️❤️❤️❤️❤️\
    \n     ❤️❤️❤️❤️❤️❤️❤️\
    \n   ❤️❤️                   ❤️❤️\
    \n ❤️❤️                       ❤️❤️\
    \n❤️❤️                         ❤️❤️\
    \n❤️❤️                         ❤️❤️\
    \n ❤️❤️                       ❤️❤️\
    \n   ❤️❤️                   ❤️❤️\
    \n      ❤️❤️❤️❤️❤️❤️❤️\
    \n            ❤️❤️❤️❤️❤️\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗                     💗💗\
    \n💗💗                     💗💗\
    \n💗💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n💗💗\
    \n💗💗\
    \n💗💗\
    \n💗💗\
    \n",
    "⁭\
    \n           💛💛💛💛💛\
    \n      💛💛💛💛💛💛💛\
    \n   💛💛                    💛💛\
    \n 💛💛                        💛💛\
    \n💛💛                           💛💛\
    \n💛💛              💛💛     💛💛\
    \n 💛💛               💛💛 💛💛\
    \n   💛💛                   💛💛\
    \n      💛💛💛💛💛💛💛💛\
    \n           💛💛💛💛💛   💛💛\
    \n",
    "⁭\
    \n💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙                     💙💙\
    \n💙💙                     💙💙\
    \n💙💙💙💙💙💙💙💙\
    \n💙💙💙💙💙💙💙\
    \n💙💙    💙💙\
    \n💙💙         💙💙\
    \n💙💙              💙💙\
    \n💙💙                  💙💙\
    \n",
    "⁭\
    \n       💟💟💟💟💟\
    \n  💟💟💟💟💟💟💟\
    \n  💟💟                 💟💟\
    \n💟💟\
    \n  💟💟💟💟💟💟\
    \n      💟💟💟💟💟💟\
    \n                            💟💟\
    \n💟💟                 💟💟\
    \n  💟💟💟💟💟💟💟\
    \n       💟💟💟💟💟\
    \n",
    "⁭\
    \n💚💚💚💚💚💚💚💚\
    \n💚💚💚💚💚💚💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n               💚💚\
    \n",
    "⁭\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n💜💜                      💜💜\
    \n  💜💜                  💜💜\
    \n      💜💜💜💜💜💜\
    \n            💜💜💜💜\
    \n",
    "\
    \n⁭❤️❤️                      ❤️❤️\
    \n\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n❤️❤️                      ❤️❤️\
    \n  ❤️❤️                  ❤️❤️\
    \n      ❤️❤️❤️❤️❤️❤️\
    \n            ❤️❤️❤️❤️\
    \n",
    "⁭\
    \n💖💖                              💖💖\
    \n  💖💖                          💖💖\
    \n    💖💖                      💖💖\
    \n      💖💖                  💖💖\
    \n         💖💖              💖💖\
    \n           💖💖         💖💖\
    \n             💖💖     💖💖\
    \n               💖💖 💖💖\
    \n                  💖💖💖\
    \n                       💖\
    \n",
    "⁭\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗                               💗💗\
    \n💗💗              💗            💗💗\
    \n 💗💗           💗💗          💗💗\
    \n 💗💗        💗💗💗       💗💗\
    \n  💗💗   💗💗  💗💗   💗💗\
    \n   💗💗💗💗      💗💗💗💗\
    \n    💗💗💗             💗💗💗\
    \n",
    "⁭\
    \n💛💛                    💛💛\
    \n   💛💛              💛💛\
    \n      💛💛        💛💛\
    \n         💛💛  💛💛\
    \n            💛💛💛\
    \n            💛💛💛\
    \n         💛💛 💛💛\
    \n      💛💛       💛💛\
    \n   💛💛             💛💛\
    \n💛💛                   💛💛\
    \n",
    "⁭\
    \n💙💙                    💙💙\
    \n   💙💙              💙💙\
    \n      💙💙        💙💙\
    \n         💙💙  💙💙\
    \n            💙💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n              💙💙\
    \n",
    "⁭\
    \n 💟💟💟💟💟💟💟\
    \n 💟💟💟💟💟💟💟\
    \n                       💟💟\
    \n                   💟💟\
    \n               💟💟\
    \n           💟💟\
    \n       💟💟\
    \n   💟💟\
    \n💟💟💟💟💟💟💟\
    \n💟💟💟💟💟💟💟\
    \n",
    "⁭\
    \n\
    \n⁭\
    \n\
    \n⁭\
    \n\
    \n",
    "⁭\
    \n       💗💗💗💗\
    \n   💗💗💗💗💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n💗💗               💗💗\
    \n   💗💗💗💗💗💗\
    \n        💗💗💗💗\
    \n",
    "⁭\
    \n          💙💙\
    \n     💙💙💙\
    \n💙💙 💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n          💙💙\
    \n     💙💙💙💙\
    \n     💙💙💙💙\
    \n",
    "⁭\
    \n    💟💟💟💟💟\
    \n  💟💟💟💟💟💟\
    \n💟💟          💟💟\
    \n                💟💟\
    \n             💟💟\
    \n          💟💟\
    \n       💟💟\
    \n    💟💟\
    \n  💟💟💟💟💟💟\
    \n  💟💟💟💟💟💟\
    \n",
    "⁭\
    \n     💛💛💛💛\
    \n  💛💛💛💛💛\
    \n💛💛         💛💛\
    \n                   💛💛\
    \n            💛💛💛\
    \n            💛💛💛\
    \n                   💛💛\
    \n💛💛         💛💛\
    \n  💛💛💛💛💛\
    \n     💛💛💛💛\
    \n",
    "⁭\
    \n                         💖💖\
    \n                    💖💖💖\
    \n              💖💖 💖💖\
    \n          💖💖     💖💖\
    \n     💖💖          💖💖\
    \n💖💖               💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n💖💖💖💖💖💖💖💖💖\
    \n                         💖💖\
    \n                         💖💖\
    \n",
    "⁭\
    \n💚💚💚💚💚💚\
    \n💚💚💚💚💚💚\
    \n💚💚\
    \n 💚💚💚💚💚\
    \n   💚💚💚💚💚\
    \n                    💚💚\
    \n                    💚💚\
    \n💚💚          💚💚\
    \n  💚💚💚💚💚\
    \n     💚💚💚💚\
    \n",
    "⁭\
    \n        💜💜💜💜\
    \n    💜💜💜💜💜\
    \n💜💜\
    \n💜💜\
    \n💜💜💜💜💜💜\
    \n💜💜💜💜💜💜💜\
    \n💜💜               💜💜\
    \n💜💜               💜💜\
    \n    💜💜💜💜💜💜\
    \n        💜💜💜💜\
    \n",
    "⁭\
    \n💗💗💗💗💗💗💗\
    \n💗💗💗💗💗💗💗\
    \n                      💗💗\
    \n                     💗💗\
    \n                   💗💗\
    \n                 💗💗\
    \n               💗💗\
    \n             💗💗\
    \n           💗💗\
    \n         💗💗\
    \n",
    "⁭\
    \n        💙💙💙💙\
    \n   💙💙💙💙💙💙\
    \n💙💙               💙💙\
    \n💙💙               💙💙\
    \n   💙💙💙💙💙💙\
    \n   💙💙💙💙💙💙\
    \n💙💙               💙💙\
    \n💙💙               💙💙\
    \n   💙💙💙💙💙💙\
    \n        💙💙💙💙\
    \n",
    "⁭\
    \n        💟💟💟💟\
    \n   💟💟💟💟💟💟\
    \n💟💟               💟💟\
    \n💟💟               💟💟\
    \n 💟💟💟💟💟💟💟\
    \n      💟💟💟💟💟💟\
    \n                         💟💟\
    \n                        💟💟\
    \n  💟💟💟💟💟💟\
    \n       💟💟💟💟\
    \n",
]

cmojis = [
    "⁭\
    \n                    {e}\
    \n                  {e}{e}\
    \n               {e}{e}{e}\
    \n            {e}{e} {e}{e}\
    \n          {e}{e}    {e}{e}\
    \n        {e}{e}       {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                 {e}{e}\
    \n  {e}{e}                    {e}{e}\
    \n{e}{e}                       {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n {e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n {e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n\
    \nㅤ                 {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                     {e}{e}\
    \n {e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n {e}{e}                        {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}{e}{e}{e}{e}\
    \n",
    "\
    \nㅤ      {e}{e}{e}{e}{e}{e}\
    \n\
    \n          {e}{e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                     {e}{e}\
    \n {e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n{e}{e}                {e}{e}{e}{e}\
    \n {e}{e}                        {e}{e}\
    \n   {e}{e}                      {e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n{e}{e}                        {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n          {e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n         {e}{e}{e}{e}{e}{e}\
    \n         {e}{e}{e}{e}{e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n                   {e}{e}\
    \n{e}{e}         {e}{e}\
    \n  {e}{e}       {e}{e}\
    \n   {e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                  {e}{e}\
    \n{e}{e}             {e}{e}\
    \n{e}{e}        {e}{e}\
    \n{e}{e}   {e}{e}\
    \n{e}{e}{e}{e}\
    \n{e}{e} {e}{e}\
    \n{e}{e}     {e}{e}\
    \n{e}{e}         {e}{e}\
    \n{e}{e}              {e}{e}\
    \n{e}{e}                   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}{e}                      {e}{e}{e}\
    \n{e}{e}{e}{e}            {e}{e}{e}{e}\
    \n{e}{e}    {e}{e}    {e}{e}    {e}{e}\
    \n{e}{e}        {e}{e}{e}         {e}{e}\
    \n{e}{e}             {e}              {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n{e}{e}                                {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                           {e}{e}\
    \n{e}{e}{e}                      {e}{e}\
    \n{e}{e}{e}{e}                 {e}{e}\
    \n{e}{e}  {e}{e}               {e}{e}\
    \n{e}{e}     {e}{e}            {e}{e}\
    \n{e}{e}         {e}{e}        {e}{e}\
    \n{e}{e}             {e}{e}    {e}{e}\
    \n{e}{e}                 {e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}{e}\
    \n{e}{e}                           {e}{e}\
    \n",
    "⁭\
    \n           {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}{e}\
    \n",
    "\
    \nㅤ       {e}{e}      {e}{e}\
    \n\
    \n           {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n{e}{e}                         {e}{e}\
    \n {e}{e}                       {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n",
    "⁭\
    \n           {e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}\
    \n   {e}{e}                    {e}{e}\
    \n {e}{e}                        {e}{e}\
    \n{e}{e}                           {e}{e}\
    \n{e}{e}              {e}{e}     {e}{e}\
    \n {e}{e}               {e}{e} {e}{e}\
    \n   {e}{e}                   {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}{e}{e}\
    \n           {e}{e}{e}{e}{e}   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}                     {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}    {e}{e}\
    \n{e}{e}         {e}{e}\
    \n{e}{e}              {e}{e}\
    \n{e}{e}                  {e}{e}\
    \n",
    "⁭\
    \n       {e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}{e}\
    \n  {e}{e}                 {e}{e}\
    \n{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n                            {e}{e}\
    \n{e}{e}                 {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}{e}\
    \n       {e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n               {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n  {e}{e}                  {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                      {e}{e}\
    \n\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n{e}{e}                      {e}{e}\
    \n  {e}{e}                  {e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n            {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                              {e}{e}\
    \n  {e}{e}                          {e}{e}\
    \n    {e}{e}                      {e}{e}\
    \n      {e}{e}                  {e}{e}\
    \n         {e}{e}              {e}{e}\
    \n           {e}{e}         {e}{e}\
    \n             {e}{e}     {e}{e}\
    \n               {e}{e} {e}{e}\
    \n                  {e}{e}{e}\
    \n                       {e}\
    \n",
    "⁭\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}                               {e}{e}\
    \n{e}{e}             {e}             {e}{e}\
    \n{e}{e}          {e}{e}           {e}{e}\
    \n{e}{e}       {e}{e}{e}         {e}{e}\
    \n{e}{e}    {e}{e}  {e}{e}     {e}{e}\
    \n {e}{e}{e}{e}        {e}{e}{e}{e}\
    \n    {e}{e}{e}              {e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}                    {e}{e}\
    \n   {e}{e}              {e}{e}\
    \n      {e}{e}        {e}{e}\
    \n         {e}{e}  {e}{e}\
    \n            {e}{e}{e}\
    \n            {e}{e}{e}\
    \n         {e}{e} {e}{e}\
    \n      {e}{e}       {e}{e}\
    \n   {e}{e}             {e}{e}\
    \n{e}{e}                   {e}{e}\
    \n",
    "⁭\
    \n{e}{e}                    {e}{e}\
    \n   {e}{e}              {e}{e}\
    \n      {e}{e}        {e}{e}\
    \n         {e}{e}  {e}{e}\
    \n            {e}{e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n              {e}{e}\
    \n",
    "⁭\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n                       {e}{e}\
    \n                   {e}{e}\
    \n               {e}{e}\
    \n           {e}{e}\
    \n       {e}{e}\
    \n   {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n\
    \n⁭\
    \n\
    \n⁭\
    \n\
    \n",
    "⁭\
    \n       {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n          {e}{e}\
    \n     {e}{e}{e}\
    \n{e}{e} {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n           {e}{e}\
    \n      {e}{e}{e}{e}\
    \n      {e}{e}{e}{e}\
    \n",
    "⁭\
    \n    {e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n{e}{e}          {e}{e}\
    \n                {e}{e}\
    \n             {e}{e}\
    \n          {e}{e}\
    \n       {e}{e}\
    \n    {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n",
    "⁭\
    \n     {e}{e}{e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n{e}{e}         {e}{e}\
    \n                   {e}{e}\
    \n            {e}{e}{e}\
    \n            {e}{e}{e}\
    \n                   {e}{e}\
    \n{e}{e}         {e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}\
    \n",
    "⁭\
    \n                         {e}{e}\
    \n                    {e}{e}{e}\
    \n              {e}{e} {e}{e}\
    \n          {e}{e}     {e}{e}\
    \n     {e}{e}          {e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}{e}{e}\
    \n                         {e}{e}\
    \n                         {e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n {e}{e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}\
    \n                    {e}{e}\
    \n                    {e}{e}\
    \n{e}{e}          {e}{e}\
    \n  {e}{e}{e}{e}{e}\
    \n     {e}{e}{e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n    {e}{e}{e}{e}{e}\
    \n{e}{e}\
    \n{e}{e}\
    \n{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n    {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n{e}{e}{e}{e}{e}{e}{e}\
    \n                      {e}{e}\
    \n                     {e}{e}\
    \n                   {e}{e}\
    \n                 {e}{e}\
    \n               {e}{e}\
    \n             {e}{e}\
    \n           {e}{e}\
    \n         {e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n        {e}{e}{e}{e}\
    \n",
    "⁭\
    \n        {e}{e}{e}{e}\
    \n   {e}{e}{e}{e}{e}{e}\
    \n{e}{e}               {e}{e}\
    \n{e}{e}               {e}{e}\
    \n {e}{e}{e}{e}{e}{e}{e}\
    \n      {e}{e}{e}{e}{e}{e}\
    \n                         {e}{e}\
    \n                        {e}{e}\
    \n  {e}{e}{e}{e}{e}{e}\
    \n       {e}{e}{e}{e}\
    \n",
]


@relahx(outgoing=True, pattern=r"^.emoji(?:\s|$)([\s\S]*)")
async def emoji(e):
    textx = await e.get_reply_message()
    message = e.pattern_match.group(1).strip()

    if message:
        pass

    elif textx:
        message = textx.text
    
    else:
        await e.edit(f"ℹ️ __Bir söz və ya mətin ver.__\n🔹 **Nümunə:** `.emoji relahx`")
        return
    
    try:
        final = "  ".join(message).lower()
        for index in final:
            if index in basemojitext:
                text = emojis[basemojitext.index(index)]
                final = final.replace(index, text)
        await e.edit(final)
    
    except:
        await e.edit(f"**❎ Bu həddindən artıq çox böyük mətndir.**")


@relahx(outgoing=True, pattern=r"^.cmoji(?:\s|$)([\s\S]*)")
async def cmoji(c):
    message = c.pattern_match.group(1).strip()

    if message:
        try:
            emoji, message = message.split(" ", 1)

        except:
            await c.edit(f"ℹ️ __Bir söz və ya mətin ver.__\n🔹 **Nümunə:** `.cmoji 🔪 relahx`")
            return

    else:
        if len(message) < 1:
            await c.edit(f"ℹ️ __Bir söz və ya mətin ver.__\n🔹 **Nümunə:** `.cmoji 🔪 relahx`")
            return

    try:
        final = "  ".join(message).lower()
        for index in final:
            if index in basemojitext:
                text = cmojis[basemojitext.index(index)].format(e=emoji)
                final = final.replace(
                    index, text
                )
        await c.edit(final)
    
    except:
        await c.edit(f"**❎ Bu həddindən artıq çox böyük mətndir.**")


CmdHelp('emojiyazi').add_command(
    'emoji', '<söz/mətn>', 'Emojilər ilə bir şey yazın!', 'emoji <istədiyiniz söz/mətn>'
).add_command(
    'cmoji <smaylik>', '<söz/mətn>', 'İstədiyiniz hər hansı bir smaylik və ya xarakter ilə bir şey yazın!', 'cmoji 👋 salam'
).add_info('**@NeonUserbot İşlədin ag sdhfssdf // Creator: @relahx**').add()
