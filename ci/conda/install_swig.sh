# if [[ "$OSTYPE" == "linux-gnu"* ]]; then
#     # Ubuntu
#     sudo apt-get update
#     sudo apt-get install build-essential procps curl file git
#     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#     brew install swig
# elif [[ "$OSTYPE" == "darwin"* ]]; then
#     # macOS
#     brew install swig
# else
#     iwr -useb get.scoop.sh | iex
#     scoop update
#     scoop bucket add main
#     scoop install main/swig
# fi

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Ubuntu
    sudo rm /usr/bin/swig*
    sudo apt-get update
    sudo apt-get install build-essential procps curl file git tree
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> $HOME/.bash_profile
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
    brew install swig
    swig -version
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install tree
    brew install gnu-sed --with-default-names
    export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"
    pip install swig
else
    pip install swig
fi

