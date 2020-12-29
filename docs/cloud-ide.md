# Creating a Could-Based Development Environment

_December 2020_

## Impetus

Earlier in the year my wife's laptop gave up the ghost. I set up a second user on my MacBook as a way to bridge our way to a fix or a replacement – a replacement that we never found a reason to find. I'd recently purchased an iPad Pro that was meeting most of my larger-device needs, and we could always pass the computer back and forth if need be. There is one glaring hole in this setup, however: writing software. Getting heads down in a side project is not particularly conducive to sharing a computer. I have a work machine, of course, but for a host of reasons I prefer not to use company-provided hardware for personal use.

This led me to a question: **Is there any reason why I couldn't develop software completely on the iPad?**

I didn't see any reason why not. With improved keyboard and trackpad support, iPadOS has become extremely comfortable for daily use. With GitHub and cloud storage, I've long since been untethered from needing any sort of persistent physical storage. There are plenty of iOS terminal emulators out there to choose from. And virtual machine hosting means I can easily spin up whatever resources I happen to need in the cloud.

I was able to create an environment (much of which is outlined in _Setting the Stage_ below) where I can write, test and build new software, with one glaring exception: **It's very hard for me to be productive writing code in a terminal editor.**

I'd initially hoped that this experiment would give me an excuse to beef up my terminal editor chops – I've worked with wizards who never touch the mouse and can create brilliant software with just a command prompt and a dream – but I came to Vim late in life. I can `:wq` my way around a configuration file or two but that's about it. There are some other editors out there – I used [micro][1] to complete the [Advent of Code][2] challenge this year – but combine a steep learning curve with sometimes challenging keyboard support between iPadOS, my emulator, mosh and terminal editor, I need a better solution.

Like most software engineers out there, my IDE setup is a very personal choice. I don't have a lot of requirements – I'm primarily write software for the web, a simple editor will do – and as such I've been using Visual Studio Code from its early days. In my latest search for a new editor I was happy to come across [`code-server`][3], a project that aims to bring a custom hosted Visual Studio Code to the browser.

Below is a chronicle of how I may be able to set up `code-server` and streamline the process spinning up a new development environment in the cloud.

[1]: https://micro-editor.github.io/
[2]: ../projects/advent-of-code/2020
[3]: https://github.com/cdr/code-server

## Goals

This iteration, aside from getting `code-server` going, I have two additional goals:

1. **Create a snapshot with as little cruft as possible.** True, DigitalOcean's rates for storing snapshots are 5¢/GB a month, but I'd rather keep things as efficient and quick. Ubuntu provides [minimal cloud images][4] that start as a bare-bones server instance, but they are not part of DigitalOcean's standard image set, so that
2. **Snapshot should be ready to start up out of the box.** I'm not interested in re-registering myself with GitHub every time I spin up a new environment, or copying IPs all over the place. This means things like ensuring all credentials exist on the snapshot and registering DNS and SSL automatically on boot.

[4]: https://wiki.ubuntu.com/Minimal

## Setting the Stage

When I originally explored an iPad development environment I made a few choices:

**Cloud Service Provider: DigitalOcean**
DigitalOcean is straightforward, easy-to-use, flexible and the prices are reasonable, but to be honest, my primary motivator in choosing them over AWS or Google Cloud was not to give even more money to Amazon or Google.

**Linux Distro: Ubuntu**

**iOS Terminal Emulator: Blink**
Blink has been my terminal of choice, as it's free and has all the features I need without trying too hard. Most importantly it supports [Mosh][15], which is essential to work around iOS dropping your SSH connection whenever the application is reaped from memory.

Mosh has its drawbacks, however – the most annoying is not maintaining scrollback history – and some time finding a better combination is in my future. I've purchased [Prompt][15] but have not tested it, mostly because it doesn't support Mosh – [Terminus][14] is another option but I'm wary of the pricing plan (see "trying too hard" above). Other options to replace Mosh is some combination of Tmux][13] and [Eternal Terminal][12].

[12]: https://eternalterminal.dev/
[13]: https://github.com/tmux/tmux/wiki
[14]: https://www.termius.com/
[15]: https://mosh.org/

## Starting From Scratch

### Create a new Droplet:

- [Create custom image in DigitalOcean][6]. The latest Ubuntu release at the time of writing is [20.10 Groovy Gorilla][5]. To save a few cents a month, this image can be removed after we spin up the Droplet.
- Create a new droplet from the custom image. Requirements for `code-server` call for [at least 2 cores and 1 GB of RAM][7]; I chose the shared 4 CPU/8 GB option at $40/month, if I run into performance issues I can try the dedicated 2 CPU option at the same price.

### Environment setup:

- Update and install packages:

  ```sh
  apt update && apt upgrade
  apt install git mosh vim zsh
  ```

- [Create a new SSH key and register with GitHub][8].
- [Install Oh My Zsh][11]. I've made my Zsh theme, profile and aliases [available in GitHub][9], so at this point I'll check out this repo and run my [profile configuration script][10].

### Set up DNS:

### Create a snapshot:

[5]: https://cloud-images.ubuntu.com/minimal/releases/groovy/
[6]: https://www.digitalocean.com/blog/custom-images/?segment=1*6k6ado*s_amp_id*RnFrLXcwb1kxalNEc05ldDV6MFpqUWdOOGtQeWdleV9wdnVKcHA5cXlqOGJYOVpKcV9ST3lqLUlKc1RXUktSTw..
[7]: https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md#requirements
[8]: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
[9]: ../profile
[10]: ../profile/configure.sh
[11]: https://ohmyz.sh/#install

## Installing `code-server`

## Conclusion
