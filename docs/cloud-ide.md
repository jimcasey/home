# Creating a Could-Based Development Environment

_December 2020_

## Impetus

Earlier in the year my wife's laptop gave up the ghost. I set up a second user on my MacBook as a way to bridge our way to a fix or a replacement – a replacement that we never found a reason to find. I'd recently purchased an iPad Pro that was meeting most of my larger-device needs, and we could always pass the computer back and forth if need be. There is one glaring hole in this setup, however: writing software. Getting heads down in a side project is not particularly conducive to sharing a computer. I have a work machine, of course, but for a host of reasons I prefer not to use company-provided hardware for personal use.

This led me to a question: **Is there any reason why I couldn't develop software completely on the iPad?**

I didn't see any reason why not. With improved keyboard and trackpad support, iPadOS has become extremely comfortable for daily use. With GitHub and cloud storage, I've long since been untethered from needing any sort of persistent physical storage. There are plenty of iOS terminal emulators out there to choose from. And virtual machine hosting means I can easily spin up whatever resources I happen to need in the cloud.

I was able to create an environment (much of which is outlined in _Setting the Stage_ below) where I can write, test and build new software, with one glaring exception: **It's very hard for me to be productive writing code in a terminal editor.**

I'd initially hoped that this experiment would give me an excuse to beef up my terminal editor chops – I've worked with wizards who never touch the mouse and can create brilliant software with just a command prompt and a dream – but I came to Vim late in life. I can `:wq` my way around a configuration file or two but that's about it. There are some other editors out there – I used [micro][1] to complete the [Advent of Code][2] challenge this year – but combine a steep learning curve with sometimes challenging keyboard support between iPadOS, my emulator, mosh and terminal editor, I need a better solution.

Like most software engineers out there, my IDE setup is a very personal choice. I don't have a lot of requirements – I'm primarily write software for the web, a simple editor will do – and as such I've been using Visual Studio Code from its early days. I've heard of various efforts to bring development to the browser (GitHub's [Codespaces][3] is too turnkey for this experiment), but in my latest search for a new editor I was happy to come across [code-server][4], a project that aims to bring a custom hosted Visual Studio Code to the browser.

Below is a chronicle of how I may be able to set up code-server and streamline the process spinning up a new development environment in the cloud.

[1]: https://micro-editor.github.io/
[2]: ../projects/advent-of-code/2020
[3]: https://code.visualstudio.com/docs/remote/codespaces
[4]: https://github.com/cdr/code-server

## Goals

## Setting the Stage

- DigitalOcean
- terminal emulator: Blink

## The Process

## Conclusion
