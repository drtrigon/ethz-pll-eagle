## Projekte
### Blattdurchmesser
[![design rule check status](https://edrc.me/api/v1/user/drtrigon/project/ethz-pll-eagle/img/status.svg)](https://edrc.me/g/drtrigon/ethz-pll-eagle)

https://gitlab.ethz.ch/PLL/Blattdurchmesser

[![projects/Blattdurchmesser/Blattdurchmesser.brd from EDRC.me](https://edrc.me/api/v1/user/drtrigon/project/ethz-pll-eagle/img/file/projects%2FBlattdurchmesser%2FBlattdurchmesser.png?ref=refs%2Fheads%2Fmaster)](https://edrc.me/g/drtrigon/ethz-pll-eagle)

https://github.com/drtrigon/ethz-pll-eagle/tree/result/pcb

## Setup

I would like to use features like CI (continous integration) keep a copy/mirror on e.g. github and more.

ETHZ GitLab could (and may be already does) support such features but I do not understand how this works.

Maintaining a copy/mirror (more precise: with 2 remotes overloaded origin) on GitHub also allows
to use GitLab and GitHub together and by that all the nice featurs on GitHub.
See also; https://steveperkins.com/migrating-projects-from-github-to-gitlab/

"Option 2: Overload Origin with Both Remotes (needs one single pull/push only)"; in order to clone
and set this repo up use:
```
$ git clone https://gitlab.ethz.ch/PLL/eagle.git
$ cd eagle
$ git remote set-url --add origin https://github.com/drtrigon/ethz-pll-eagle.git
```
you can check the settings with:
```
$ git remote -v
origin  https://gitlab.ethz.ch/PLL/eagle.git (fetch)
origin  https://gitlab.ethz.ch/PLL/eagle.git (push)
origin  https://github.com/drtrigon/ethz-pll-eagle.git (push)
```

### Enable EDRC.ME for a Repository (for Eagle)
http://www.edrc.me/docs/

### Further Info
https://github.com/drtrigon/eagle
