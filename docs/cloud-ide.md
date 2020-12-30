# Creating a Could-Based Development Environment

## Impetus

Earlier in the year my wife's laptop gave up the ghost. I set up a second user on my MacBook as a way to bridge our way to a fix or a replacement – that we never got around to. I'd recently purchased an iPad Pro that meets most of my needs, and we pass the computer back and forth as needed. There's a hole in this setup, however: writing software. Getting heads down in a side project is not conducive to sharing a computer. I have a work machine, of course, but for a host of reasons I'd rather not to use company-provided hardware for personal use.

I had a thought: **Why couldn't I develop software completely on the iPad?**

I didn't see any reason why not. With improved keyboard and trackpad support, iPadOS has become bery comfortable for daily use. With GitHub and cloud storage, I've long since been untethered from needing persistent physical storage. There are options for iOS and iPadOS terminal emulators. And VM hosting means I can easily spin up whatever resources I happen to need in the cloud.

So I set out to create an environment where I could write, test and build new software, finding moderate success and one big exception: **It's very hard for me to be productive writing code in a terminal editor.**

I'd hoped that this experiment would give me an excuse to beef up my terminal editor chops – I've worked with wizards who never touch the mouse and write brilliant software with just a command prompt and a dream – but I came to Vim late in life. Sure, I can `:wq` my way around a configuration file, but that's about it. Sure, there are other editors – I used [micro][1] to complete the [Advent of Code][2] challenge this year – but a steep learning curve combined with sometimes challenging keyboard support, I need a better solution.

Like most people who write software, my IDE setup is a extremely personal choice. I'm not one with a lot of requirements – I'm primarily write software for the web, a simple editor will do – and as such I've been using Visual Studio Code from its early days. In my latest search for a new editor I was happy to come across [`code-server`][3], a project that aims to bring a custom hosted Visual Studio Code to the browser.

Below is a chronicle of how I may be able to set up `code-server` and streamline the process spinning up a new development environment in the cloud.

## Goals

This iteration, aside from getting `code-server` going, I have two additional goals:

1. **Create a snapshot with as little cruft as possible.** True, DigitalOcean's rates for storing snapshots are 5¢/GB a month, but I'd rather keep things as efficient and quick.
2. **Snapshot should be ready to start up out of the box.** I'm not interested in re-registering myself with GitHub every time I spin up a new environment, or copying IPs all over the place. This means things like ensuring all credentials exist on the snapshot and registering DNS and SSL automatically on boot.

## Setting the Stage

When I originally explored an iPad development environment I made a few choices:

**Cloud Service Provider: DigitalOcean**
DigitalOcean is straightforward, easy-to-use, flexible and the prices are reasonable, but to be honest, my primary motivator in choosing them over AWS or Google Cloud was not to give even more money to Amazon or Google.

**Linux Distro: Ubuntu**
Easy, frequent updates and package availability made this a simple choice. Making things lightweight is a priority, so another distribution might be more appropriate, although Ubuntu provides [minimal cloud images][4] we can use to build up bare-bones server instance.

**iOS Terminal Emulator: Blink**
Blink has been my terminal of choice, as it's free and has all the features I need without trying too hard. Most importantly it supports [Mosh][5], which is essential to work around iOS dropping your SSH connection whenever the application is reaped from memory.

Mosh has its drawbacks, however – the most annoying is not maintaining scrollback history – and some time finding a better combination is in my future. I've purchased [Prompt][6] but have not tested it, mostly because it doesn't support Mosh – [Terminus][7] is another option but I'm wary of the pricing plan (see "trying too hard" above). Other options to replace Mosh is some combination of [Tmux][8] and [Eternal Terminal][9].

## Starting From Scratch

To create a foundation to install `code-server`, let's build up a new droplet from scratch:

### Create a new droplet:

[Create custom image in DigitalOcean][10] (the latest Ubuntu release at the time of writing is [20.10 Groovy Gorilla][11]), then create a new droplet from the custom image. To save a few cents a month, this image can be removed after we spin up the droplet.

> I'd originally chosen the shared 4 CPU/8 GB option for my droplet, only to find out that snapshots can't be restored to droplets [smaller than the original instance][19]. As requirements for `code-server` call for [at least 2 cores and 1 GB of RAM][12], I started with the smaller shared 2 CPU/2 GB option.

### Environment setup:

Update and install packages:

```sh
apt update && apt upgrade
apt install git mosh vim zsh
```

> Note that all commands here assume we're running under the `root` user; if you're running under another user you'll have to `sudo` everything up.

I've made my Zsh theme, profile and aliases [available in this repo][15], so at this point [create a new SSH key and register with GitHub][13], clone and run my [profile configuration script][16].

### Set up DNS:

Install DDClient:

```sh
apt install ddclient
```

I use Namecheap as my DNS provider; DDClient will run a configuration script, but [this reference][17] is useful for determining the correct properties, but for reference, this is the `/etc/ddclient.conf` that worked for me:

```conf
use=web web=https://dynamicdns.park-your-domain.com/getip
protocol=namecheap
server=dynamicdns.park-your-domain.com
login=mydomain.com
password=[redacted]
mysubdomain
```

Finally, we can run a test to see if it's working:

```sh
ddclient -query
```

### Create a snapshot:

- At this point we're good to create a [snapshot of our droplet][18].

## Installing `code-server`

`code-server` has a [detailed guide][20] for setting up an instance on Google Cloud.

First step is to install the server:

```sh
curl -fsSL https://code-server.dev/install.sh | sh
systemctl enable --now code-server@$USER
```

Unfortunately we can't use SSH forwarding as we want to access this on an iPad, the guide offers a few ways to get expose `code-server` to the internet securely. As I've got a little experience with NGINX, I went with [that method][22] here.

Installing NGINX and Certbot:

```sh
sudo apt install -y nginx certbot python3-certbot-nginx
```

Save the following configuration at `/etc/nginx/sites-available/code-server`:

```
server {
  listen 80;
  listen [::]:80;
  server_name mydomain.com;

  location / {
    proxy_pass http://localhost:8080/;
    proxy_set_header Host $host;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection upgrade;
    proxy_set_header Accept-Encoding gzip;
  }
}
```

Finally, enable the configuration:

```sh
ln -s /etc/nginx/sites-available/code-server /etc/nginx/sites-enabled/code-server
certbot --non-interactive --redirect --agree-tos --nginx -d mydomain.com -m me@example.com
```

...and success! Navigating to `https://mydomain.com` loads Visual Studio Code in the browser.

### Bonus:

Since I've added my VSCode [settings and keybindings files][23] into this repo, I went ahead and created a link to the configuration directory for `code-server`:

```sh
ln -s ~/home/profile/vscode/settings.json ~/.local/share/code-server/User/settings.json
ln -s ~/home/profile/vscode/keybindings.json ~/.local/share/code-server/User/keybindings.json
```

## Conclusion

As the [`code-server` docs attest][21], creating software on an iPad is not for the faint of heart. I still don't know how well this setup will work for me, with iPadOS constantly dropping the application state and the like. I find myself with half an eye on the new M1 MacBook Air – $999 is not a ton of money for an actual keyboard and a real operating system with real VSCode and a real terminal, after all.

But in the meantime, as I'm not working ton of side projects, we'll give this a try. I'll check back in when I've done a little more playing around.

_Jim – December 2020_

[1]: https://micro-editor.github.io/
[2]: ../projects/advent-of-code/2020
[3]: https://github.com/cdr/code-server
[4]: https://wiki.ubuntu.com/Minimal
[5]: https://mosh.org/
[6]: https://panic.com/prompt/
[7]: https://www.termius.com/
[8]: https://github.com/tmux/tmux/wiki
[9]: https://eternalterminal.dev/
[10]: https://www.digitalocean.com/blog/custom-images/
[11]: https://cloud-images.ubuntu.com/minimal/releases/groovy/
[19]: https://www.digitalocean.com/docs/images/snapshots/how-to/create-and-restore-droplets/#create-new-droplets-from-a-snapshot
[12]: https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md#requirements
[15]: ../profile
[13]: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh
[16]: ../profile/configure.sh
[17]: https://www.namecheap.com/support/knowledgebase/article.aspx/583/11/how-do-i-configure-ddclient/
[18]: https://www.digitalocean.com/docs/images/snapshots/how-to/snapshot-droplets/
[20]: https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md
[22]: https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md#nginx
[23]: ../profile/vscode
[21]: https://github.com/cdr/code-server/blob/v3.8.0/doc/ipad.md#recommendations
