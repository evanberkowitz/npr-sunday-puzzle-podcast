## The NPR Sunday Puzzle

[The Sunday Puzzle][npr] is a feature on [Weekend Edition Sunday][weekend-edition-sunday]
where a contestant plays an on-air quiz with [Will Shortz][shortz].

The puzzle _used_ to be available as a podcast.  But, for whatever reason, NPR
stopped offering it in podcast form factor.  It is available as [an RSS feed][npr-rss]
but without the audio, it does not do me much good---I need those sweet sweet
puzzles piped directly into my ears.

When invoked, `npr-puzzle` will

 - scrape the NPR Sunday Puzzle page,
 - lex the results into podcast descriptions
 - write a podcast xml to $REPO/npr-puzzle.xml

If invoked with `--publish`, will add the changes to that xml to the repository, and push.

Using `launchd` with `npr-puzzle.plist` will cause this to happen once a week,
after the puzzle is published online, so that the XML will be updated for easy listening.

[npr]:                      https://npr.org/puzzle
[npr-rss]:                  https://feeds.npr.org/4473090/rss.xml
[weekend-edition-sunday]:   https://www.npr.org/programs/weekend-edition-sunday/
[shortz]:                   https://willshortz.com/
