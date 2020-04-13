#!/usr/bin/env python

import os
import argparse

script_dir = os.path.dirname(os.path.abspath(__file__))

# TODO: We can lookup https://github.com/tmux/tmux/blob/3.0/options-table.c#L143

# Extracted from http://man7.org/linux/man-pages/man1/tmux.1.html#OPTIONS
# Some options are ignored(see commented items)
server_options = (
    "buffer-limit",
    # 'command-alias',  # Ignored: is array
    "default-terminal",
    "escape-time",
    "exit-empty",
    "exit-unattached",
    "focus-events",
    "history-file",
    "message-limit",
    "set-clipboard",
    # 'terminal-overrides',  # Ignored: is array
    # 'user-keys',  # Ignored: is array
)

session_options = (
    "activity-action",
    "assume-paste-time",
    "base-index",
    "bell-action",
    "default-command",
    # 'default-shell',  # Ignored: to set $SHELL correctly
    "default-size",
    "destroy-unattached",
    "detach-on-destroy",
    "display-panes-active-colour",
    "display-panes-colour",
    "display-panes-time",
    "display-time",
    "history-limit",
    "key-table",
    "lock-after-time",
    "lock-command",
    "message-command-style",
    "message-style",
    "mouse",
    "prefix",
    "prefix2",
    "renumber-windows",
    "repeat-time",
    "set-titles",
    "set-titles-string",
    "silence-action",
    "status",
    # 'status-format'  # Ignored: is array
    "status-interval",
    "status-justify",
    "status-keys",
    "status-left",
    "status-left-length",
    "status-left-style",
    "status-position",
    "status-right",
    "status-right-length",
    "status-right-style",
    "status-style",
    # 'update-environment',  # Ignored: is array
    "visual-activity",
    "visual-bell",
    "visual-silence",
    "word-separators",
)

window_options = (
    "aggressive-resize",
    "automatic-rename",
    "automatic-rename-format",
    "clock-mode-colour",
    "clock-mode-style",
    "main-pane-height",
    "main-pane-width",
    "mode-keys",
    "mode-style",
    "monitor-activity",
    "monitor-bell",
    "monitor-silence",
    "other-pane-height",
    "other-pane-width",
    "pane-active-border-style",
    "pane-base-index",
    "pane-border-format",
    "pane-border-status",
    "pane-border-style",
    "synchronize-panes",
    "window-status-activity-style",
    "window-status-bell-style",
    "window-status-current-format",
    "window-status-current-style",
    "window-status-format",
    "window-status-last-style",
    "window-status-separator",
    "window-status-style",
    "window-size",
    "wrap-search",
    "xterm-keys",
)

pane_options = (
    "allow-rename",
    "alternate-screen",
    "remain-on-exit",
    "window-active-style",
    "window-style",
)

# Copied from https://github.com/tmux/tmux/blob/2.9/key-bindings.c
initial_key_bindings = (
    "bind C-b send-prefix",
    "bind C-o rotate-window",
    "bind C-z suspend-client",
    "bind Space next-layout",
    "bind ! break-pane",
    "bind '\"' split-window",
    "bind '#' list-buffers",
    "bind '$' command-prompt -I'#S' \"rename-session -- '%%'\"",
    "bind % split-window -h",
    'bind & confirm-before -p"kill-window #W? (y/n)" kill-window',
    'bind "\'" command-prompt -pindex "select-window -t \':%%\'"',
    "bind ( switch-client -p",
    "bind ) switch-client -n",
    "bind , command-prompt -I'#W' \"rename-window -- '%%'\"",
    "bind - delete-buffer",
    "bind . command-prompt \"move-window -t '%%'\"",
    "bind 0 select-window -t:=0",
    "bind 1 select-window -t:=1",
    "bind 2 select-window -t:=2",
    "bind 3 select-window -t:=3",
    "bind 4 select-window -t:=4",
    "bind 5 select-window -t:=5",
    "bind 6 select-window -t:=6",
    "bind 7 select-window -t:=7",
    "bind 8 select-window -t:=8",
    "bind 9 select-window -t:=9",
    "bind : command-prompt",
    "bind \\; last-pane",
    "bind = choose-buffer -Z",
    "bind ? list-keys",
    "bind D choose-client -Z",
    "bind E select-layout -E",
    "bind L switch-client -l",
    "bind M select-pane -M",
    "bind [ copy-mode",
    "bind ] paste-buffer",
    "bind c new-window",
    "bind d detach-client",
    "bind f command-prompt \"find-window -Z -- '%%'\"",
    "bind i display-message",
    "bind l last-window",
    "bind m select-pane -m",
    "bind n next-window",
    "bind o select-pane -t:.+",
    "bind p previous-window",
    "bind q display-panes",
    "bind r refresh-client",
    "bind s choose-tree -Zs",
    "bind t clock-mode",
    "bind w choose-tree -Zw",
    'bind x confirm-before -p"kill-pane #P? (y/n)" kill-pane',
    "bind z resize-pane -Z",
    "bind '{' swap-pane -U",
    "bind '}' swap-pane -D",
    "bind '~' show-messages",
    "bind PPage copy-mode -u",
    "bind -r Up select-pane -U",
    "bind -r Down select-pane -D",
    "bind -r Left select-pane -L",
    "bind -r Right select-pane -R",
    "bind M-1 select-layout even-horizontal",
    "bind M-2 select-layout even-vertical",
    "bind M-3 select-layout main-horizontal",
    "bind M-4 select-layout main-vertical",
    "bind M-5 select-layout tiled",
    "bind M-n next-window -a",
    "bind M-o rotate-window -D",
    "bind M-p previous-window -a",
    "bind -r S-Up refresh-client -U 10",
    "bind -r S-Down refresh-client -D 10",
    "bind -r S-Left refresh-client -L 10",
    "bind -r S-Right refresh-client -R 10",
    "bind -r DC refresh-client -c",
    "bind -r M-Up resize-pane -U 5",
    "bind -r M-Down resize-pane -D 5",
    "bind -r M-Left resize-pane -L 5",
    "bind -r M-Right resize-pane -R 5",
    "bind -r C-Up resize-pane -U",
    "bind -r C-Down resize-pane -D",
    "bind -r C-Left resize-pane -L",
    "bind -r C-Right resize-pane -R",
    "bind -n MouseDown1Pane select-pane -t=\\; send-keys -M",
    "bind -n MouseDrag1Border resize-pane -M",
    "bind -n MouseDown1Status select-window -t=",
    "bind -n WheelDownStatus next-window",
    "bind -n WheelUpStatus previous-window",
    "bind -n MouseDrag1Pane if -Ft= '#{mouse_any_flag}' 'if -Ft= \"#{pane_in_mode}\" \"copy-mode -M\" \"send-keys -M\"' 'copy-mode -M'",
    "bind -n WheelUpPane if -Ft= '#{mouse_any_flag}' 'send-keys -M' 'if -Ft= \"#{pane_in_mode}\" \"send-keys -M\" \"copy-mode -et=\"'",
    'bind -n MouseDown3StatusRight display-menu -t= -xM -yS -T "#[align=centre]#{client_name}" '
    " 'Detach' 'd' {detach-client}"
    " 'Detach & Kill' 'X' {detach-client -P}"
    " 'Detach Others' 'o' {detach-client -a}"
    " ''"
    " 'Lock' 'l' {lock-client}",
    'bind -n MouseDown3StatusLeft display-menu -t= -xM -yS -T "#[align=centre]#{session_name}" '
    " 'Next' 'n' {switch-client -n}"
    " 'Previous' 'p' {switch-client -p}"
    " ''"
    " 'Renumber' 'N' {move-window -r}"
    " 'Rename' 'n' {command-prompt -I \"#S\" \"rename-session -- '%%'\"}"
    " ''"
    " 'New Session' 's' {new-session}"
    " 'New Window' 'w' {new-window}",
    'bind -n MouseDown3Status display-menu -t= -xW -yS -T "#[align=centre]#{window_index}:#{window_name}" '
    " 'Swap Left' 'l' {swap-window -t:-1}"
    " 'Swap Right' 'r' {swap-window -t:+1}"
    " '#{?pane_marked_set,,-}Swap Marked' 's' {swap-window}"
    " ''"
    " 'Kill' 'X' {kill-window}"
    " 'Respawn' 'R' {respawn-window -k}"
    " '#{?pane_marked,Unmark,Mark}' 'm' {select-pane -m}"
    " 'Rename' 'n' {command-prompt -I \"#W\" \"rename-window -- '%%'\"}"
    " ''"
    " 'New After' 'w' {new-window -a}"
    " 'New At End' 'W' {new-window}",
    'bind < display-menu -xW -yS -T "#[align=centre]#{window_index}:#{window_name}" '
    " 'Swap Left' 'l' {swap-window -t:-1}"
    " 'Swap Right' 'r' {swap-window -t:+1}"
    " '#{?pane_marked_set,,-}Swap Marked' 's' {swap-window}"
    " ''"
    " 'Kill' 'X' {kill-window}"
    " 'Respawn' 'R' {respawn-window -k}"
    " '#{?pane_marked,Unmark,Mark}' 'm' {select-pane -m}"
    " 'Rename' 'n' {command-prompt -I \"#W\" \"rename-window -- '%%'\"}"
    " ''"
    " 'New After' 'w' {new-window -a}"
    " 'New At End' 'W' {new-window}",
    "bind -n MouseDown3Pane if -Ft= '#{||:#{mouse_any_flag},#{pane_in_mode}}' 'select-pane -t=; send-keys -M' {display-menu -t= -xM -yM -T \"#[align=centre]#{pane_index} (#{pane_id})\" "
    " '#{?mouse_word,Search For #[underscore]#{=/9/...:mouse_word},}' 'C-r' {copy-mode -t=; send -Xt= search-backward \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Type #[underscore]#{=/9/...:mouse_word},}' 'C-y' {send-keys -l -- \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Copy #[underscore]#{=/9/...:mouse_word},}' 'c' {set-buffer -- \"#{q:mouse_word}\"}"
    " '#{?mouse_line,Copy Line,}' 'l' {set-buffer -- \"#{q:mouse_line}\"}"
    " ''"
    " 'Horizontal Split' 'h' {split-window -h}"
    " 'Vertical Split' 'v' {split-window -v}"
    " ''"
    " 'Swap Up' 'u' {swap-pane -U}"
    " 'Swap Down' 'd' {swap-pane -D}"
    " '#{?pane_marked_set,,-}Swap Marked' 's' {swap-pane}"
    " ''"
    " 'Kill' 'X' {kill-pane}"
    " 'Respawn' 'R' {respawn-pane -k}"
    " '#{?pane_marked,Unmark,Mark}' 'm' {select-pane -m}"
    " '#{?window_zoomed_flag,Unzoom,Zoom}' 'z' {resize-pane -Z}"
    "}",
    'bind -n M-MouseDown3Pane display-menu -t= -xM -yM -T "#[align=centre]#{pane_index} (#{pane_id})" '
    " '#{?mouse_word,Search For #[underscore]#{=/9/...:mouse_word},}' 'C-r' {copy-mode -t=; send -Xt= search-backward \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Type #[underscore]#{=/9/...:mouse_word},}' 'C-y' {send-keys -l -- \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Copy #[underscore]#{=/9/...:mouse_word},}' 'c' {set-buffer -- \"#{q:mouse_word}\"}"
    " '#{?mouse_line,Copy Line,}' 'l' {set-buffer -- \"#{q:mouse_line}\"}"
    " ''"
    " 'Horizontal Split' 'h' {split-window -h}"
    " 'Vertical Split' 'v' {split-window -v}"
    " ''"
    " 'Swap Up' 'u' {swap-pane -U}"
    " 'Swap Down' 'd' {swap-pane -D}"
    " '#{?pane_marked_set,,-}Swap Marked' 's' {swap-pane}"
    " ''"
    " 'Kill' 'X' {kill-pane}"
    " 'Respawn' 'R' {respawn-pane -k}"
    " '#{?pane_marked,Unmark,Mark}' 'm' {select-pane -m}"
    " '#{?window_zoomed_flag,Unzoom,Zoom}' 'z' {resize-pane -Z}",
    'bind > display-menu -xP -yP -T "#[align=centre]#{pane_index} (#{pane_id})" '
    " '#{?mouse_word,Search For #[underscore]#{=/9/...:mouse_word},}' 'C-r' {copy-mode -t=; send -Xt= search-backward \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Type #[underscore]#{=/9/...:mouse_word},}' 'C-y' {send-keys -l -- \"#{q:mouse_word}\"}"
    " '#{?mouse_word,Copy #[underscore]#{=/9/...:mouse_word},}' 'c' {set-buffer -- \"#{q:mouse_word}\"}"
    " '#{?mouse_line,Copy Line,}' 'l' {set-buffer -- \"#{q:mouse_line}\"}"
    " ''"
    " 'Horizontal Split' 'h' {split-window -h}"
    " 'Vertical Split' 'v' {split-window -v}"
    " ''"
    " 'Swap Up' 'u' {swap-pane -U}"
    " 'Swap Down' 'd' {swap-pane -D}"
    " '#{?pane_marked_set,,-}Swap Marked' 's' {swap-pane}"
    " ''"
    " 'Kill' 'X' {kill-pane}"
    " 'Respawn' 'R' {respawn-pane -k}"
    " '#{?pane_marked,Unmark,Mark}' 'm' {select-pane -m}"
    " '#{?window_zoomed_flag,Unzoom,Zoom}' 'z' {resize-pane -Z}",
    "bind -Tcopy-mode C-Space send -X begin-selection",
    "bind -Tcopy-mode C-a send -X start-of-line",
    "bind -Tcopy-mode C-c send -X cancel",
    "bind -Tcopy-mode C-e send -X end-of-line",
    "bind -Tcopy-mode C-f send -X cursor-right",
    "bind -Tcopy-mode C-b send -X cursor-left",
    "bind -Tcopy-mode C-g send -X clear-selection",
    "bind -Tcopy-mode C-k send -X copy-end-of-line",
    "bind -Tcopy-mode C-n send -X cursor-down",
    "bind -Tcopy-mode C-p send -X cursor-up",
    "bind -Tcopy-mode C-r command-prompt -ip'(search up)' -I'#{pane_search_string}' 'send -X search-backward-incremental \"%%%\"'",
    "bind -Tcopy-mode C-s command-prompt -ip'(search down)' -I'#{pane_search_string}' 'send -X search-forward-incremental \"%%%\"'",
    "bind -Tcopy-mode C-v send -X page-down",
    "bind -Tcopy-mode C-w send -X copy-selection-and-cancel",
    "bind -Tcopy-mode Escape send -X cancel",
    "bind -Tcopy-mode Space send -X page-down",
    "bind -Tcopy-mode , send -X jump-reverse",
    "bind -Tcopy-mode \\; send -X jump-again",
    "bind -Tcopy-mode F command-prompt -1p'(jump backward)' 'send -X jump-backward \"%%%\"'",
    "bind -Tcopy-mode N send -X search-reverse",
    "bind -Tcopy-mode R send -X rectangle-toggle",
    "bind -Tcopy-mode T command-prompt -1p'(jump to backward)' 'send -X jump-to-backward \"%%%\"'",
    "bind -Tcopy-mode f command-prompt -1p'(jump forward)' 'send -X jump-forward \"%%%\"'",
    "bind -Tcopy-mode g command-prompt -p'(goto line)' 'send -X goto-line \"%%%\"'",
    "bind -Tcopy-mode n send -X search-again",
    "bind -Tcopy-mode q send -X cancel",
    "bind -Tcopy-mode t command-prompt -1p'(jump to forward)' 'send -X jump-to-forward \"%%%\"'",
    "bind -Tcopy-mode Home send -X start-of-line",
    "bind -Tcopy-mode End send -X end-of-line",
    "bind -Tcopy-mode MouseDown1Pane select-pane",
    "bind -Tcopy-mode MouseDrag1Pane select-pane\\; send -X begin-selection",
    "bind -Tcopy-mode MouseDragEnd1Pane send -X copy-selection-and-cancel",
    "bind -Tcopy-mode WheelUpPane select-pane\\; send -N5 -X scroll-up",
    "bind -Tcopy-mode WheelDownPane select-pane\\; send -N5 -X scroll-down",
    "bind -Tcopy-mode DoubleClick1Pane select-pane\\; send -X select-word",
    "bind -Tcopy-mode TripleClick1Pane select-pane\\; send -X select-line",
    "bind -Tcopy-mode NPage send -X page-down",
    "bind -Tcopy-mode PPage send -X page-up",
    "bind -Tcopy-mode Up send -X cursor-up",
    "bind -Tcopy-mode Down send -X cursor-down",
    "bind -Tcopy-mode Left send -X cursor-left",
    "bind -Tcopy-mode Right send -X cursor-right",
    "bind -Tcopy-mode M-1 command-prompt -Np'(repeat)' -I1 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-2 command-prompt -Np'(repeat)' -I2 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-3 command-prompt -Np'(repeat)' -I3 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-4 command-prompt -Np'(repeat)' -I4 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-5 command-prompt -Np'(repeat)' -I5 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-6 command-prompt -Np'(repeat)' -I6 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-7 command-prompt -Np'(repeat)' -I7 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-8 command-prompt -Np'(repeat)' -I8 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-9 command-prompt -Np'(repeat)' -I9 'send -N \"%%%\"'",
    "bind -Tcopy-mode M-< send -X history-top",
    "bind -Tcopy-mode M-> send -X history-bottom",
    "bind -Tcopy-mode M-R send -X top-line",
    "bind -Tcopy-mode M-b send -X previous-word",
    "bind -Tcopy-mode C-M-b send -X previous-matching-bracket",
    "bind -Tcopy-mode M-f send -X next-word-end",
    "bind -Tcopy-mode C-M-f send -X next-matching-bracket",
    "bind -Tcopy-mode M-m send -X back-to-indentation",
    "bind -Tcopy-mode M-r send -X middle-line",
    "bind -Tcopy-mode M-v send -X page-up",
    "bind -Tcopy-mode M-w send -X copy-selection-and-cancel",
    "bind -Tcopy-mode 'M-{' send -X previous-paragraph",
    "bind -Tcopy-mode 'M-}' send -X next-paragraph",
    "bind -Tcopy-mode M-Up send -X halfpage-up",
    "bind -Tcopy-mode M-Down send -X halfpage-down",
    "bind -Tcopy-mode C-Up send -X scroll-up",
    "bind -Tcopy-mode C-Down send -X scroll-down",
    "bind -Tcopy-mode-vi C-c send -X cancel",
    "bind -Tcopy-mode-vi C-d send -X halfpage-down",
    "bind -Tcopy-mode-vi C-e send -X scroll-down",
    "bind -Tcopy-mode-vi C-b send -X page-up",
    "bind -Tcopy-mode-vi C-f send -X page-down",
    "bind -Tcopy-mode-vi C-h send -X cursor-left",
    "bind -Tcopy-mode-vi C-j send -X copy-selection-and-cancel",
    "bind -Tcopy-mode-vi Enter send -X copy-selection-and-cancel",
    "bind -Tcopy-mode-vi C-u send -X halfpage-up",
    "bind -Tcopy-mode-vi C-v send -X rectangle-toggle",
    "bind -Tcopy-mode-vi C-y send -X scroll-up",
    "bind -Tcopy-mode-vi Escape send -X clear-selection",
    "bind -Tcopy-mode-vi Space send -X begin-selection",
    "bind -Tcopy-mode-vi '$' send -X end-of-line",
    "bind -Tcopy-mode-vi , send -X jump-reverse",
    "bind -Tcopy-mode-vi / command-prompt -p'(search down)' 'send -X search-forward \"%%%\"'",
    "bind -Tcopy-mode-vi 0 send -X start-of-line",
    "bind -Tcopy-mode-vi 1 command-prompt -Np'(repeat)' -I1 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 2 command-prompt -Np'(repeat)' -I2 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 3 command-prompt -Np'(repeat)' -I3 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 4 command-prompt -Np'(repeat)' -I4 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 5 command-prompt -Np'(repeat)' -I5 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 6 command-prompt -Np'(repeat)' -I6 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 7 command-prompt -Np'(repeat)' -I7 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 8 command-prompt -Np'(repeat)' -I8 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi 9 command-prompt -Np'(repeat)' -I9 'send -N \"%%%\"'",
    "bind -Tcopy-mode-vi : command-prompt -p'(goto line)' 'send -X goto-line \"%%%\"'",
    "bind -Tcopy-mode-vi \\; send -X jump-again",
    "bind -Tcopy-mode-vi ? command-prompt -p'(search up)' 'send -X search-backward \"%%%\"'",
    "bind -Tcopy-mode-vi A send -X append-selection-and-cancel",
    "bind -Tcopy-mode-vi B send -X previous-space",
    "bind -Tcopy-mode-vi D send -X copy-end-of-line",
    "bind -Tcopy-mode-vi E send -X next-space-end",
    "bind -Tcopy-mode-vi F command-prompt -1p'(jump backward)' 'send -X jump-backward \"%%%\"'",
    "bind -Tcopy-mode-vi G send -X history-bottom",
    "bind -Tcopy-mode-vi H send -X top-line",
    "bind -Tcopy-mode-vi J send -X scroll-down",
    "bind -Tcopy-mode-vi K send -X scroll-up",
    "bind -Tcopy-mode-vi L send -X bottom-line",
    "bind -Tcopy-mode-vi M send -X middle-line",
    "bind -Tcopy-mode-vi N send -X search-reverse",
    "bind -Tcopy-mode-vi T command-prompt -1p'(jump to backward)' 'send -X jump-to-backward \"%%%\"'",
    "bind -Tcopy-mode-vi V send -X select-line",
    "bind -Tcopy-mode-vi W send -X next-space",
    "bind -Tcopy-mode-vi ^ send -X back-to-indentation",
    "bind -Tcopy-mode-vi b send -X previous-word",
    "bind -Tcopy-mode-vi e send -X next-word-end",
    "bind -Tcopy-mode-vi f command-prompt -1p'(jump forward)' 'send -X jump-forward \"%%%\"'",
    "bind -Tcopy-mode-vi g send -X history-top",
    "bind -Tcopy-mode-vi h send -X cursor-left",
    "bind -Tcopy-mode-vi j send -X cursor-down",
    "bind -Tcopy-mode-vi k send -X cursor-up",
    "bind -Tcopy-mode-vi l send -X cursor-right",
    "bind -Tcopy-mode-vi n send -X search-again",
    "bind -Tcopy-mode-vi o send -X other-end",
    "bind -Tcopy-mode-vi q send -X cancel",
    "bind -Tcopy-mode-vi t command-prompt -1p'(jump to forward)' 'send -X jump-to-forward \"%%%\"'",
    "bind -Tcopy-mode-vi v send -X rectangle-toggle",
    "bind -Tcopy-mode-vi w send -X next-word",
    "bind -Tcopy-mode-vi '{' send -X previous-paragraph",
    "bind -Tcopy-mode-vi '}' send -X next-paragraph",
    "bind -Tcopy-mode-vi % send -X next-matching-bracket",
    "bind -Tcopy-mode-vi MouseDown1Pane select-pane",
    "bind -Tcopy-mode-vi MouseDrag1Pane select-pane\\; send -X begin-selection",
    "bind -Tcopy-mode-vi MouseDragEnd1Pane send -X copy-selection-and-cancel",
    "bind -Tcopy-mode-vi WheelUpPane select-pane\\; send -N5 -X scroll-up",
    "bind -Tcopy-mode-vi WheelDownPane select-pane\\; send -N5 -X scroll-down",
    "bind -Tcopy-mode-vi DoubleClick1Pane select-pane\\; send -X select-word",
    "bind -Tcopy-mode-vi TripleClick1Pane select-pane\\; send -X select-line",
    "bind -Tcopy-mode-vi BSpace send -X cursor-left",
    "bind -Tcopy-mode-vi NPage send -X page-down",
    "bind -Tcopy-mode-vi PPage send -X page-up",
    "bind -Tcopy-mode-vi Up send -X cursor-up",
    "bind -Tcopy-mode-vi Down send -X cursor-down",
    "bind -Tcopy-mode-vi Left send -X cursor-left",
    "bind -Tcopy-mode-vi Right send -X cursor-right",
    "bind -Tcopy-mode-vi C-Up send -X scroll-up",
    "bind -Tcopy-mode-vi C-Down send -X scroll-down",
)

if __name__ == "__main__":
    prefix = ""
    filename = "tmux-reset"

    parser = argparse.ArgumentParser(description="Creates a tmux-reset config")
    parser.add_argument(
        "-t",
        "--tpm",
        action="store_true",
        help="build for .tmux file for TPM compatibility",
    )
    args = parser.parse_args()

    if args.tpm:
        prefix = "tmux "
        filename += ".tmux"
        header = """#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
"""

    with open(os.path.join(script_dir, filename), "w") as f:
        if args.tpm:
            f.write("%s\n" % header)

        options = server_options + session_options + window_options + pane_options
        for option_name in options:
            f.write("%sset-option -ug %s\n" % (prefix, option_name))

        f.write("%sunbind-key -a\n" % prefix)

        for binding in initial_key_bindings:
            if args.tpm:
                binding = binding.replace(" \\; ", ' "\\;" ')
            f.write("%s%s\n" % (prefix, binding))
