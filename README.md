# tmux-reset

No more restarting tmux to apply changed configurations.
Just put `source-file /path/to/tmux-reset` at the top of your `.tmux.conf`.

## What is it?

tmux-reset is very similar to `reset.css` or `normalize.css`.
It unsets tmux options to their defaults and unbinds all of the bound keys,
and then applies the [default key bindings][default-key-bindings].
After that, you are free to change options you'd like to.

## Installation

### Manual Installation

1. Download `tmux-reset` file and put it in somewhere(for example, ~/.tmux/reset).
You can rename it to whatever you want. Even the file extension isn't important.

2. Open your `.tmux.conf` and put the following line at the top:
    ```tmux
    source-file ~/.tmux/reset
    ```
    Don't forget to change `~/.tmux/reset` to the location you put the `tmux-reset`.

3. That's it. Now whenever you reload your configuration(`.tmux.conf`),
you don't need to kill your tmux server and restart the server to
reset the other options to the default.

### Installation Script

Here is a shorthand for the manual installation above:
```bash
curl -Lo ~/.tmux/reset --create-dirs \
    https://raw.githubusercontent.com/hallazzang/tmux-reset/master/tmux-reset
```

Actually, it doesn't do any 'installation' stuffs. It just downloads the file
into `~/.tmux/reset`. You still have to put `source-file ~/.tmux/reset` at
the top of your `.tmux.conf`.

[default-key-bindings]: https://github.com/tmux/tmux/blob/2.6/key-bindings.c#L158-L385
