## The NPR Sunday Puzzle

[The Sunday Puzzle][npr] is a feature on [Weekend Edition Sunday][weekend-edition-sunday]
where a contestant plays an on-air quiz with [Will Shortz][shortz].
[The podcast built here][podcast] can be constructed, enjoyed, or subscribed to by anyone wishing to enjoy
the puzzle.

### To Subscribe

Most podcast applications allow you to subscribe directly via [the URL of the feed][podcast].
On MacOS, for example, in the Podcasts app, the option is under `File > Add a Show by URL...`.
In the iOS Podcasts app, if you're looking at the `Library` pane,
there is an `Edit` option in the upper-right corner which, when clicked,
also presents an `Add a Show by URL...` option.

Some players may implement a stricter protocol than is supported by hosting the podcast as raw content on github.
I am exploring other hosting options to allow these podcatchers to successfully subscribe.

### Technical Details

The puzzle _used_ to be available as a podcast.  But, for whatever reason, NPR
stopped offering it in podcast form factor.  It is available as [an RSS feed][npr-rss]
but without the audio, it does not do me much good---I need those sweet sweet
puzzles piped directly into my ears.

When invoked, [`npr-puzzle`][pages] will

 - scrape the NPR Sunday Puzzle page,
 - lex the results into podcast descriptions
 - write a podcast xml to $REPO/npr-puzzle.xml

If invoked with `--publish`, will add the changes to that xml to the repository, and push.

Since I am running this myself, the feed will be pushed to [this repository][repo],
so that one may subscribe directly to [the podcast][podcast].

Using `launchd` with `npr-puzzle.plist` will cause this to happen once a week,
after the puzzle is published online, so that the XML will be updated for easy listening.

[npr]:                      https://npr.org/puzzle
[npr-rss]:                  https://feeds.npr.org/4473090/rss.xml
[pages]:                    https://evanberkowitz.github.io/npr-sunday-puzzle-podcast/
[podcast]:                  https://raw.githubusercontent.com/evanberkowitz/npr-sunday-puzzle-podcast/master/npr-puzzle.xml
[repo]:                     https://github.com/evanberkowitz/npr-sunday-puzzle-podcast
[weekend-edition-sunday]:   https://www.npr.org/programs/weekend-edition-sunday/
[shortz]:                   https://willshortz.com/
