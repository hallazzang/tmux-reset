#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
        
tmux set-option -ug buffer-limit
tmux set-option -ug default-terminal
tmux set-option -ug escape-time
tmux set-option -ug exit-unattached
tmux set-option -ug focus-events
tmux set-option -ug history-file
tmux set-option -ug message-limit
tmux set-option -ug set-clipboard
tmux set-option -ug activity-action
tmux set-option -ug assume-paste-time
tmux set-option -ug base-index
tmux set-option -ug bell-action
tmux set-option -ug default-command
tmux set-option -ug destroy-unattached
tmux set-option -ug detach-on-destroy
tmux set-option -ug display-panes-active-colour
tmux set-option -ug display-panes-colour
tmux set-option -ug display-panes-time
tmux set-option -ug display-time
tmux set-option -ug history-limit
tmux set-option -ug key-table
tmux set-option -ug lock-after-time
tmux set-option -ug lock-command
tmux set-option -ug message-command-style
tmux set-option -ug message-style
tmux set-option -ug mouse
tmux set-option -ug prefix
tmux set-option -ug prefix2
tmux set-option -ug renumber-windows
tmux set-option -ug repeat-time
tmux set-option -ug set-titles
tmux set-option -ug set-titles-string
tmux set-option -ug silence-action
tmux set-option -ug status
tmux set-option -ug status-interval
tmux set-option -ug status-justify
tmux set-option -ug status-keys
tmux set-option -ug status-left
tmux set-option -ug status-left-length
tmux set-option -ug status-left-style
tmux set-option -ug status-position
tmux set-option -ug status-right
tmux set-option -ug status-right-length
tmux set-option -ug status-right-style
tmux set-option -ug visual-activity
tmux set-option -ug visual-bell
tmux set-option -ug visual-silence
tmux set-option -ug word-separators
tmux set-window-option -ug aggressive-resize
tmux set-window-option -ug allow-rename
tmux set-window-option -ug alternate-screen
tmux set-window-option -ug automatic-rename
tmux set-window-option -ug automatic-rename-format
tmux set-window-option -ug clock-mode-colour
tmux set-window-option -ug clock-mode-style
tmux set-window-option -ug force-height
tmux set-window-option -ug force-width
tmux set-window-option -ug main-pane-height
tmux set-window-option -ug main-pane-width
tmux set-window-option -ug mode-style
tmux set-window-option -ug monitor-activity
tmux set-window-option -ug monitor-bell
tmux set-window-option -ug monitor-silence
tmux set-window-option -ug other-pane-height
tmux set-window-option -ug other-pane-width
tmux set-window-option -ug pane-active-border-style
tmux set-window-option -ug pane-base-index
tmux set-window-option -ug pane-border-format
tmux set-window-option -ug pane-border-status
tmux set-window-option -ug pane-border-style
tmux set-window-option -ug remain-on-exit
tmux set-window-option -ug synchronize-panes
tmux set-window-option -ug window-active-style
tmux set-window-option -ug window-status-activity-style
tmux set-window-option -ug window-status-bell-style
tmux set-window-option -ug window-status-current-format
tmux set-window-option -ug window-status-current-style
tmux set-window-option -ug window-status-format
tmux set-window-option -ug window-status-last-style
tmux set-window-option -ug window-status-separator
tmux set-window-option -ug window-status-style
tmux set-window-option -ug window-style
tmux set-window-option -ug wrap-search
tmux set-window-option -ug xterm-keys
tmux unbind-key -a
tmux bind C-b send-prefix
tmux bind C-o rotate-window
tmux bind C-z suspend-client
tmux bind Space next-layout
tmux bind ! break-pane
tmux bind '"' split-window
tmux bind '#' list-buffers
tmux bind '$' command-prompt -I'#S' "rename-session '%%'"
tmux bind % split-window -h
tmux bind & confirm-before -p"kill-window #W? (y/n)" kill-window
tmux bind "'" command-prompt -pindex "select-window -t ':%%'"
tmux bind ( switch-client -p
tmux bind ) switch-client -n
tmux bind , command-prompt -I'#W' "rename-window '%%'"
tmux bind - delete-buffer
tmux bind . command-prompt "move-window -t '%%'"
tmux bind 0 select-window -t:=0
tmux bind 1 select-window -t:=1
tmux bind 2 select-window -t:=2
tmux bind 3 select-window -t:=3
tmux bind 4 select-window -t:=4
tmux bind 5 select-window -t:=5
tmux bind 6 select-window -t:=6
tmux bind 7 select-window -t:=7
tmux bind 8 select-window -t:=8
tmux bind 9 select-window -t:=9
tmux bind : command-prompt
tmux bind \; last-pane
tmux bind = choose-buffer
tmux bind ? list-keys
tmux bind D choose-client
tmux bind L switch-client -l
tmux bind M select-pane -M
tmux bind [ copy-mode
tmux bind ] paste-buffer
tmux bind c new-window
tmux bind d detach-client
tmux bind f command-prompt "find-window '%%'"
tmux bind i display-message
tmux bind l last-window
tmux bind m select-pane -m
tmux bind n next-window
tmux bind o select-pane -t:.+
tmux bind p previous-window
tmux bind q display-panes
tmux bind r refresh-client
tmux bind s choose-tree -s
tmux bind t clock-mode
tmux bind w choose-tree -w
tmux bind x confirm-before -p"kill-pane #P? (y/n)" kill-pane
tmux bind z resize-pane -Z
tmux bind { swap-pane -U
tmux bind } swap-pane -D
tmux bind '~' show-messages
tmux bind PPage copy-mode -u
tmux bind -r Up select-pane -U
tmux bind -r Down select-pane -D
tmux bind -r Left select-pane -L
tmux bind -r Right select-pane -R
tmux bind M-1 select-layout even-horizontal
tmux bind M-2 select-layout even-vertical
tmux bind M-3 select-layout main-horizontal
tmux bind M-4 select-layout main-vertical
tmux bind M-5 select-layout tiled
tmux bind M-n next-window -a
tmux bind M-o rotate-window -D
tmux bind M-p previous-window -a
tmux bind -r M-Up resize-pane -U 5
tmux bind -r M-Down resize-pane -D 5
tmux bind -r M-Left resize-pane -L 5
tmux bind -r M-Right resize-pane -R 5
tmux bind -r C-Up resize-pane -U
tmux bind -r C-Down resize-pane -D
tmux bind -r C-Left resize-pane -L
tmux bind -r C-Right resize-pane -R
tmux bind -n MouseDown1Pane select-pane -t=\; send-keys -M
tmux bind -n MouseDrag1Border resize-pane -M
tmux bind -n MouseDown1Status select-window -t=
tmux bind -n WheelDownStatus next-window
tmux bind -n WheelUpStatus previous-window
tmux bind -n MouseDrag1Pane if -Ft= '#{mouse_any_flag}' 'if -Ft= "#{pane_in_mode}" "copy-mode -M" "send-keys -M"' 'copy-mode -M'
tmux bind -n MouseDown3Pane if-shell -Ft= '#{mouse_any_flag}' 'select-pane -t=; send-keys -M' 'select-pane -mt='
tmux bind -n WheelUpPane if-shell -Ft= '#{mouse_any_flag}' 'send-keys -M' 'if -Ft= "#{pane_in_mode}" "send-keys -M" "copy-mode -et="'
tmux bind -Tcopy-mode C-Space send -X begin-selection
tmux bind -Tcopy-mode C-a send -X start-of-line
tmux bind -Tcopy-mode C-c send -X cancel
tmux bind -Tcopy-mode C-e send -X end-of-line
tmux bind -Tcopy-mode C-f send -X cursor-right
tmux bind -Tcopy-mode C-b send -X cursor-left
tmux bind -Tcopy-mode C-g send -X clear-selection
tmux bind -Tcopy-mode C-k send -X copy-end-of-line
tmux bind -Tcopy-mode C-n send -X cursor-down
tmux bind -Tcopy-mode C-p send -X cursor-up
tmux bind -Tcopy-mode C-r command-prompt -ip'(search up)' -I'#{pane_search_string}' 'send -X search-backward-incremental "%%%"'
tmux bind -Tcopy-mode C-s command-prompt -ip'(search down)' -I'#{pane_search_string}' 'send -X search-forward-incremental "%%%"'
tmux bind -Tcopy-mode C-v send -X page-down
tmux bind -Tcopy-mode C-w send -X copy-selection-and-cancel
tmux bind -Tcopy-mode Escape send -X cancel
tmux bind -Tcopy-mode Space send -X page-down
tmux bind -Tcopy-mode , send -X jump-reverse
tmux bind -Tcopy-mode \; send -X jump-again
tmux bind -Tcopy-mode F command-prompt -1p'(jump backward)' 'send -X jump-backward "%%%"'
tmux bind -Tcopy-mode N send -X search-reverse
tmux bind -Tcopy-mode R send -X rectangle-toggle
tmux bind -Tcopy-mode T command-prompt -1p'(jump to backward)' 'send -X jump-to-backward "%%%"'
tmux bind -Tcopy-mode f command-prompt -1p'(jump forward)' 'send -X jump-forward "%%%"'
tmux bind -Tcopy-mode g command-prompt -p'(goto line)' 'send -X goto-line "%%%"'
tmux bind -Tcopy-mode n send -X search-again
tmux bind -Tcopy-mode q send -X cancel
tmux bind -Tcopy-mode t command-prompt -1p'(jump to forward)' 'send -X jump-to-forward "%%%"'
tmux bind -Tcopy-mode Home send -X start-of-line
tmux bind -Tcopy-mode End send -X end-of-line
tmux bind -Tcopy-mode MouseDown1Pane select-pane
tmux bind -Tcopy-mode MouseDrag1Pane select-pane\; send -X begin-selection
tmux bind -Tcopy-mode MouseDragEnd1Pane send -X copy-selection-and-cancel
tmux bind -Tcopy-mode WheelUpPane select-pane\; send -N5 -X scroll-up
tmux bind -Tcopy-mode WheelDownPane select-pane\; send -N5 -X scroll-down
tmux bind -Tcopy-mode DoubleClick1Pane select-pane\; send -X select-word
tmux bind -Tcopy-mode TripleClick1Pane select-pane\; send -X select-line
tmux bind -Tcopy-mode NPage send -X page-down
tmux bind -Tcopy-mode PPage send -X page-up
tmux bind -Tcopy-mode Up send -X cursor-up
tmux bind -Tcopy-mode Down send -X cursor-down
tmux bind -Tcopy-mode Left send -X cursor-left
tmux bind -Tcopy-mode Right send -X cursor-right
tmux bind -Tcopy-mode M-1 command-prompt -Np'(repeat)' -I1 'send -N "%%%"'
tmux bind -Tcopy-mode M-2 command-prompt -Np'(repeat)' -I2 'send -N "%%%"'
tmux bind -Tcopy-mode M-3 command-prompt -Np'(repeat)' -I3 'send -N "%%%"'
tmux bind -Tcopy-mode M-4 command-prompt -Np'(repeat)' -I4 'send -N "%%%"'
tmux bind -Tcopy-mode M-5 command-prompt -Np'(repeat)' -I5 'send -N "%%%"'
tmux bind -Tcopy-mode M-6 command-prompt -Np'(repeat)' -I6 'send -N "%%%"'
tmux bind -Tcopy-mode M-7 command-prompt -Np'(repeat)' -I7 'send -N "%%%"'
tmux bind -Tcopy-mode M-8 command-prompt -Np'(repeat)' -I8 'send -N "%%%"'
tmux bind -Tcopy-mode M-9 command-prompt -Np'(repeat)' -I9 'send -N "%%%"'
tmux bind -Tcopy-mode M-< send -X history-top
tmux bind -Tcopy-mode M-> send -X history-bottom
tmux bind -Tcopy-mode M-R send -X top-line
tmux bind -Tcopy-mode M-b send -X previous-word
tmux bind -Tcopy-mode M-f send -X next-word-end
tmux bind -Tcopy-mode M-m send -X back-to-indentation
tmux bind -Tcopy-mode M-r send -X middle-line
tmux bind -Tcopy-mode M-v send -X page-up
tmux bind -Tcopy-mode M-w send -X copy-selection-and-cancel
tmux bind -Tcopy-mode M-{ send -X previous-paragraph
tmux bind -Tcopy-mode M-} send -X next-paragraph
tmux bind -Tcopy-mode M-Up send -X halfpage-up
tmux bind -Tcopy-mode M-Down send -X halfpage-down
tmux bind -Tcopy-mode C-Up send -X scroll-up
tmux bind -Tcopy-mode C-Down send -X scroll-down
tmux bind -Tcopy-mode-vi C-c send -X cancel
tmux bind -Tcopy-mode-vi C-d send -X halfpage-down
tmux bind -Tcopy-mode-vi C-e send -X scroll-down
tmux bind -Tcopy-mode-vi C-b send -X page-up
tmux bind -Tcopy-mode-vi C-f send -X page-down
tmux bind -Tcopy-mode-vi C-h send -X cursor-left
tmux bind -Tcopy-mode-vi C-j send -X copy-selection-and-cancel
tmux bind -Tcopy-mode-vi Enter send -X copy-selection-and-cancel
tmux bind -Tcopy-mode-vi C-u send -X halfpage-up
tmux bind -Tcopy-mode-vi C-v send -X rectangle-toggle
tmux bind -Tcopy-mode-vi C-y send -X scroll-up
tmux bind -Tcopy-mode-vi Escape send -X clear-selection
tmux bind -Tcopy-mode-vi Space send -X begin-selection
tmux bind -Tcopy-mode-vi '$' send -X end-of-line
tmux bind -Tcopy-mode-vi , send -X jump-reverse
tmux bind -Tcopy-mode-vi / command-prompt -p'(search down)' 'send -X search-forward "%%%"'
tmux bind -Tcopy-mode-vi 0 send -X start-of-line
tmux bind -Tcopy-mode-vi 1 command-prompt -Np'(repeat)' -I1 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 2 command-prompt -Np'(repeat)' -I2 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 3 command-prompt -Np'(repeat)' -I3 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 4 command-prompt -Np'(repeat)' -I4 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 5 command-prompt -Np'(repeat)' -I5 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 6 command-prompt -Np'(repeat)' -I6 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 7 command-prompt -Np'(repeat)' -I7 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 8 command-prompt -Np'(repeat)' -I8 'send -N "%%%"'
tmux bind -Tcopy-mode-vi 9 command-prompt -Np'(repeat)' -I9 'send -N "%%%"'
tmux bind -Tcopy-mode-vi : command-prompt -p'(goto line)' 'send -X goto-line "%%%"'
tmux bind -Tcopy-mode-vi \; send -X jump-again
tmux bind -Tcopy-mode-vi ? command-prompt -p'(search up)' 'send -X search-backward "%%%"'
tmux bind -Tcopy-mode-vi A send -X append-selection-and-cancel
tmux bind -Tcopy-mode-vi B send -X previous-space
tmux bind -Tcopy-mode-vi D send -X copy-end-of-line
tmux bind -Tcopy-mode-vi E send -X next-space-end
tmux bind -Tcopy-mode-vi F command-prompt -1p'(jump backward)' 'send -X jump-backward "%%%"'
tmux bind -Tcopy-mode-vi G send -X history-bottom
tmux bind -Tcopy-mode-vi H send -X top-line
tmux bind -Tcopy-mode-vi J send -X scroll-down
tmux bind -Tcopy-mode-vi K send -X scroll-up
tmux bind -Tcopy-mode-vi L send -X bottom-line
tmux bind -Tcopy-mode-vi M send -X middle-line
tmux bind -Tcopy-mode-vi N send -X search-reverse
tmux bind -Tcopy-mode-vi T command-prompt -1p'(jump to backward)' 'send -X jump-to-backward "%%%"'
tmux bind -Tcopy-mode-vi V send -X select-line
tmux bind -Tcopy-mode-vi W send -X next-space
tmux bind -Tcopy-mode-vi ^ send -X back-to-indentation
tmux bind -Tcopy-mode-vi b send -X previous-word
tmux bind -Tcopy-mode-vi e send -X next-word-end
tmux bind -Tcopy-mode-vi f command-prompt -1p'(jump forward)' 'send -X jump-forward "%%%"'
tmux bind -Tcopy-mode-vi g send -X history-top
tmux bind -Tcopy-mode-vi h send -X cursor-left
tmux bind -Tcopy-mode-vi j send -X cursor-down
tmux bind -Tcopy-mode-vi k send -X cursor-up
tmux bind -Tcopy-mode-vi l send -X cursor-right
tmux bind -Tcopy-mode-vi n send -X search-again
tmux bind -Tcopy-mode-vi o send -X other-end
tmux bind -Tcopy-mode-vi q send -X cancel
tmux bind -Tcopy-mode-vi t command-prompt -1p'(jump to forward)' 'send -X jump-to-forward "%%%"'
tmux bind -Tcopy-mode-vi v send -X rectangle-toggle
tmux bind -Tcopy-mode-vi w send -X next-word
tmux bind -Tcopy-mode-vi { send -X previous-paragraph
tmux bind -Tcopy-mode-vi } send -X next-paragraph
tmux bind -Tcopy-mode-vi MouseDown1Pane select-pane
tmux bind -Tcopy-mode-vi MouseDrag1Pane select-pane\; send -X begin-selection
tmux bind -Tcopy-mode-vi MouseDragEnd1Pane send -X copy-selection-and-cancel
tmux bind -Tcopy-mode-vi WheelUpPane select-pane\; send -N5 -X scroll-up
tmux bind -Tcopy-mode-vi WheelDownPane select-pane\; send -N5 -X scroll-down
tmux bind -Tcopy-mode-vi DoubleClick1Pane select-pane\; send -X select-word
tmux bind -Tcopy-mode-vi TripleClick1Pane select-pane\; send -X select-line
tmux bind -Tcopy-mode-vi BSpace send -X cursor-left
tmux bind -Tcopy-mode-vi NPage send -X page-down
tmux bind -Tcopy-mode-vi PPage send -X page-up
tmux bind -Tcopy-mode-vi Up send -X cursor-up
tmux bind -Tcopy-mode-vi Down send -X cursor-down
tmux bind -Tcopy-mode-vi Left send -X cursor-left
tmux bind -Tcopy-mode-vi Right send -X cursor-right
tmux bind -Tcopy-mode-vi C-Up send -X scroll-up
tmux bind -Tcopy-mode-vi C-Down send -X scroll-down
