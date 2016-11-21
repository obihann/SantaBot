# SantaBot

Built around [SantasList](https://github.com/obihann/santaslist) this is a Errbot plugin to help organize your secret santa parties.

## Commands

* pairs - list the pairs of all santas

    ```
    >>> !pairs
    frank franklyn <---> bob bober
    jeff hann <---> george the dog
    ```
    
## Setup

* Sample Data

    To get started create a file called `people.yml` and put it in the root errbot folder. Here is what it could contain:
    ```
    --- 
    people: 
      - 
        name: "jeff hann"
        username: "@obihann"
      - 
        name: "bob bober"
        username: "@bob"
      - 
        name: "frank franklyn"
        username: "@franky"
      - 
        name: "george the dog"
        username: "@george"
    ```
