# tmux-reset

Easy way to reset all options to default in tmux(3.0)

## What is it?

**tmux-reset** is very similar to `reset.css` or `normalize.css` for CSS.
When you source this file through `source-file` command, it resets all tmux options to their defaults.
It also unbinds all bound keys then applies the [default key bindings].
From clean state, you can apply any changes to your tmux as usual.

## Installation

There are two ways to install and activate this script.

### Using TPM

Add this line in your `.tmux.conf`:

```tmux
set -g @plugin 'hallazzang/tmux-reset'
```

### Manual Installation

1. Download [tmux-reset] file and put it in somewhere, for example, `~/.tmux/reset`:
    ```bash
    $ curl -Lo ~/.tmux/reset --create-dirs \
        https://raw.githubusercontent.com/hallazzang/tmux-reset/3.0/tmux-reset
    ```

2. Include this line at the top of your `.tmux.conf`:
    ```tmux
    source-file ~/.tmux/reset
    ```
    Don't forget to change `~/.tmux/reset` above to actual location of downloaded file.

That's it. Now whenever you reload your `.tmux.conf`,
you don't need to kill your tmux server and restart it to reset options.

## Alternative Versions

If you're using other version of tmux, please check [tags].

Here are currently supported versions:

- [3.0](https://github.com/hallazzang/tmux-reset/tree/3.0)
- [3.0a](https://github.com/hallazzang/tmux-reset/tree/3.0a)
- [2.9](https://github.com/hallazzang/tmux-reset/tree/2.9)

[tags]: https://github.com/hallazzang/tmux-reset/tags
[tmux-reset]: https://github.com/hallazzang/tmux-reset/blob/3.0/tmux-reset
