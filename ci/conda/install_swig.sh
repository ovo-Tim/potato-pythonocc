if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Ubuntu
    sudo apt-get update
    sudo apt-get install build-essential procps curl file git
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    brew install swig
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install swig
else
    iwr -useb get.scoop.sh | iex
    scoop update
    scoop bucket add main
    scoop install main/swig
fi