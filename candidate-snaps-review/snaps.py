#!/usr/bin/python

# table of snaps we are interested in
#("name", "stable build url", "beta build url", "edge build url, "stable yaml url", "beta yaml url", "edge yaml url", "upstream git vcs", "track"),
# BRANCH is replaced in the script by the currently used branch
normalsnaps = [
# ("authenticator", "https://launchpad.net/~desktop-snappers/+snap/authenticator", None, None, "https://raw.githubusercontent.com/ubuntu/authenticator/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/World/Authenticator", None),
 ("cheese", "https://launchpad.net/~desktop-snappers/+snap/cheese", None, None, "https://raw.githubusercontent.com/ubuntu/cheese/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/cheese/", None),
 ("eog", "https://launchpad.net/~desktop-snappers/+snap/eog", None, None, "https://raw.githubusercontent.com/ubuntu/eog/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/eog/", None),
 ("epiphany", "https://launchpad.net/~desktop-snappers/+snap/epiphany", None, "https://launchpad.net/~desktop-snappers/+snap/epiphany-edge", "https://raw.githubusercontent.com/ubuntu/epiphany/stable/snapcraft.yaml", None, "https://raw.githubusercontent.com/ubuntu/epiphany/edge/snapcraft.yaml", "https://gitlab.gnome.org/GNOME/epiphany", None),
 ("evince", "https://launchpad.net/~desktop-snappers/+snap/evince", None, None, "https://raw.githubusercontent.com/ubuntu/evince/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/evince/", None),
 ("five-or-more", "https://launchpad.net/~desktop-snappers/+snap/five-or-more", None, None, "https://raw.githubusercontent.com/ubuntu/five-or-more/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/five-or-more", None),
# ("fractal", "https://launchpad.net/~desktop-snappers/+snap/fractal", None, None, "https://git.launchpad.net/~desktop-snappers/fractal/+git/main/plain/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/fractal", None),
 ("gedit", "https://launchpad.net/~desktop-snappers/+snap/gedit", None, None, "https://raw.githubusercontent.com/ubuntu/gedit/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gedit", None),
 ("glade", "https://launchpad.net/~desktop-snappers/+snap/glade", None, None, "https://raw.githubusercontent.com/ubuntu/glade/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/glade", None),
 ("gnome-2048", "https://launchpad.net/~desktop-snappers/+snap/gnome-2048", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-2048/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-2048", None),
 ("gnome-boxes", "https://launchpad.net/~desktop-snappers/+snap/gnome-boxes", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-boxes/stable/snap/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-boxes", None),
 ("gnome-calculator", "https://launchpad.net/~desktop-snappers/+snap/gnome-calculator", None, "https://launchpad.net/~desktop-snappers/+snap/gnome-calculator-edge", "https://raw.githubusercontent.com/ubuntu/gnome-calculator/stable/snapcraft.yaml", None, "https://raw.githubusercontent.com/ubuntu/gnome-calculator/edge/snapcraft.yaml", "https://gitlab.gnome.org/GNOME/gnome-calculator", None),
 ("gnome-characters", "https://launchpad.net/~desktop-snappers/+snap/gnome-characters", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-characters/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-characters", None),
 ("gnome-chess", "https://launchpad.net/~desktop-snappers/+snap/gnome-chess", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-chess/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-chess", None),
 ("gnome-clocks", "https://launchpad.net/~desktop-snappers/+snap/gnome-clocks", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-clocks/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-clocks", None),
 ("gnome-contacts", "https://launchpad.net/~desktop-snappers/+snap/gnome-contacts", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-contacts/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-contacts", None),
 ("gnome-dictionary", "https://launchpad.net/~desktop-snappers/+snap/gnome-dictionary", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-dictionary/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-dictionary", None),
 ("gnome-font-viewer", "https://launchpad.net/~desktop-snappers/+snap/gnome-font-viewer", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-font-viewer/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-font-viewer", None),
 ("gnome-hitori", "https://launchpad.net/~desktop-snappers/+snap/gnome-hitori", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-hitori/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/hitori", None),
 ("gnome-klotski", "https://launchpad.net/~desktop-snappers/+snap/gnome-klotski", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-klotski/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-klotski", None),
 ("gnome-logs", "https://launchpad.net/~desktop-snappers/+snap/gnome-logs", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-logs/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-logs", None),
 ("gnome-mahjongg", "https://launchpad.net/~desktop-snappers/+snap/gnome-mahjongg", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-mahjongg/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-mahjongg", None),
 ("gnome-mines", "https://launchpad.net/~desktop-snappers/+snap/gnome-mines", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-mines/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-mines", None),
 ("gnome-nibbles", "https://launchpad.net/~desktop-snappers/+snap/gnome-nibbles", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-nibbles/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-nibbles", None),
 ("gnome-recipes", "https://launchpad.net/~desktop-snappers/+snap/gnome-recipes", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-recipes/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/recipes", None),
 ("gnome-robots", "https://launchpad.net/~desktop-snappers/+snap/gnome-robots", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-robots/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-robots", None),
 ("gnome-sudoku", "https://launchpad.net/~desktop-snappers/+snap/gnome-sudoku", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-sudoku/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-sudoku", None),
# ("gnome-sound-recorder", None, None, None, None, None, None),
 ("gnome-system-monitor", "https://launchpad.net/~desktop-snappers/+snap/gnome-system-monitor", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-system-monitor/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-system-monitor", None),
 ("gnome-taquin", "https://launchpad.net/~desktop-snappers/+snap/gnome-taquin", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-taquin/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-taquin", None),
 ("gnome-text-editor", "https://launchpad.net/~desktop-snappers/gnome-text-editor/+snap/gnome-text-editor", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-text-editor/stable/snap/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-text-editor", None),
 ("gnome-tetravex", "https://launchpad.net/~desktop-snappers/+snap/gnome-tetravex", None, None, "https://raw.githubusercontent.com/ubuntu/gnome-tetravex/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/gnome-tetravex", None),
 ("iagno", "https://launchpad.net/~desktop-snappers/+snap/iagno", None, None, "https://raw.githubusercontent.com/ubuntu/iagno/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/iagno", None),
 ("lightsoff", "https://launchpad.net/~desktop-snappers/+snap/lightsoff", None, None, "https://raw.githubusercontent.com/ubuntu/lightsoff/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/lightsoff", None),
 ("quadrapassel", "https://launchpad.net/~desktop-snappers/+snap/quadrapassel", None, None, "https://raw.githubusercontent.com/ubuntu/quadrapassel/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/quadrapassel", None),
# ("remmina", None, None, None, None, None, None),
 ("swell-foop", "https://launchpad.net/~desktop-snappers/+snap/swell-foop", None, None, "https://raw.githubusercontent.com/ubuntu/swell-foop/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/swell-foop", None),
 ("tali", "https://launchpad.net/~desktop-snappers/+snap/tali", None, None, "https://raw.githubusercontent.com/ubuntu/tali/stable/snapcraft.yaml", None, None, "https://gitlab.gnome.org/GNOME/tali", None),
 ("cherrytree", None, None, "https://launchpad.net/~hellsworth/+snap/cherrytree", None, None, None, None, None),
 ("libreoffice", "https://launchpad.net/~desktop-snappers/+snap/libreoffice-snap", None, None, "https://raw.githubusercontent.com/ubuntu/libreoffice/7.2/snapcraft.yaml", None, None, None, None),
 ("thunderbird", "https://launchpad.net/~desktop-snappers/+snap/thunderbird", "https://launchpad.net/~desktop-snappers/+snap/thunderbird-beta", None, "https://raw.githubusercontent.com/ubuntu/thunderbird/stable/snapcraft.yaml", "https://raw.githubusercontent.com/ubuntu/thunderbird/beta/snapcraft.yaml", None, None, None),
 ("chromium", "https://launchpad.net/~chromium-team/+snap/chromium-snap-from-source-stable", "https://launchpad.net/~chromium-team/+snap/chromium-snap-from-source-beta", "https://launchpad.net/~chromium-team/+snap/chromium-snap-from-source-dev", "https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/plain/snapcraft.yaml?h=stable", "https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/plain/snapcraft.yaml?h=beta","https://git.launchpad.net/~chromium-team/chromium-browser/+git/snap-from-source/plain/snapcraft.yaml?h=dev", None, None),
 ("firefox", "https://launchpad.net/~mozilla-snaps/firefox/+snap/firefox-snap-stable/", "https://launchpad.net/~mozilla-snaps/firefox/+snap/firefox-snap-beta", None, "https://raw.githubusercontent.com/canonical/firefox-snap/stable/snapcraft.yaml", "https://raw.githubusercontent.com/canonical/firefox-snap/beta/snapcraft.yaml", "https://github.com/canonical/firefox-snap/blob/nightly/snapcraft.yaml", None, None),
 ("steam", "https://launchpad.net/~desktop-snappers/steam-snap/+snap/steam", None, None, "https://github.com/canonical/steam-snap/blob/main/snap/snapcraft.yaml" , None, None, None, None),
]
specialsnaps = [
("gnome-3-26-1604", "https://launchpad.net/~ubuntu-desktop/+snap/gnome-3-26-1604", None, None, "https://bazaar.launchpad.net/~ubuntu-desktop/+junk/gnome-3-26-1604/download/head:/snapcraft.yaml", None, None, None, None),
("gnome-3-28-1804", "https://launchpad.net/~desktop-snappers/+snap/gnome-3-28-1804", None, None, "https://git.launchpad.net/gnome-3-28-1804/plain/snapcraft.yaml", None, None, None, None),
("gnome-3-34-1804", "https://launchpad.net/~desktop-snappers/+snap/gnome-3-34-1804", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-3-34-1804", None, None, None, None),
("gnome-3-34-1804-sdk", "https://launchpad.net/~desktop-snappers/+snap/gnome-3-34-1804-sdk", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-3-34-1804-sdk", None, None, None, None),
("gnome-3-38-2004", "https://launchpad.net/~desktop-snappers/+snap/gnome-3-38-2004", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-3-38-2004", None, None, None, None),
("gnome-3-38-2004-sdk", "https://launchpad.net/~desktop-snappers/+snap/gnome-3-38-2004-sdk", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-3-38-2004-sdk", None, None, None, None),
("gnome-42-2204", "https://launchpad.net/~desktop-snappers/+snap/gnome-42-2204", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-42-2204", None, None, None, None),
("gnome-42-2204-sdk", "https://launchpad.net/~desktop-snappers/+snap/gnome-42-2204-sdk", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-42-2204-sdk", None, None, None, None),
("gnome-46-2404", "https://launchpad.net/~desktop-snappers/+snap/gnome-46-2404", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-46-2404", None, None, None, None),
("gnome-46-2404-sdk", "https://launchpad.net/~desktop-snappers/+snap/gnome-46-2404-sdk", None, None, "https://git.launchpad.net/gnome-sdk/plain/snapcraft.yaml?h=gnome-46-2404-sdk", None, None, None, None),
("gtk-common-themes", "https://launchpad.net/~desktop-snappers/+snap/gtk-common-themes", None, None, "https://gitlab.gnome.org/Community/Ubuntu/gtk-common-themes/-/raw/main/snap/snapcraft.yaml", None, None, None, None),
("snap-store", "https://launchpad.net/~desktop-snappers/+snap/snap-store-stable", None, "https://launchpad.net/~desktop-snappers/+snap/snap-store", "https://git.launchpad.net/snap-store-desktop/plain/snap/snapcraft.yaml?h=snap-store-stable", None, "https://git.launchpad.net/snap-store-desktop/plain/snap/snapcraft.yaml", None, None),
("snapd-desktop-integration", "https://launchpad.net/~desktop-snappers/+snap/snapd-desktop-integration", None, None, "https://raw.githubusercontent.com/canonical/snapd-desktop-integration/main/snap/snapcraft.yaml", None, None, None, None),
("ubuntu-desktop-bootstrap", None, None, "https://launchpad.net/~ubuntu-desktop/ubuntu-desktop-provision/+snap/ubuntu-desktop-bootstrap", None, None, "https://git.launchpad.net/ubuntu-desktop-provision/plain/ci/snap/bootstrap/snapcraft.yaml", None, None),
("gaming-graphics-core22", "https://launchpad.net/~desktop-snappers/gaming-graphics/+snap/oibaf-latest-core22", None, None, "https://github.com/canonical/gaming-graphics/tree/oibaf-latest-core22", None, None, None, "oibaf-latest"),
("gaming-graphics-core22", "https://launchpad.net/~desktop-snappers/gaming-graphics/+snap/kisak-fresh-core22", None, None, "https://github.com/canonical/gaming-graphics/tree/kisak-fresh-core22", None, None, None, "kisak-fresh"),
("gaming-graphics-core22", "https://launchpad.net/~desktop-snappers/gaming-graphics/+snap/kisak-turtle-core22", None, None, "https://github.com/canonical/gaming-graphics/tree/kisak-turtle-core22", None, None, None, "kisak-turtle"),
]

snapstable = normalsnaps + specialsnaps
