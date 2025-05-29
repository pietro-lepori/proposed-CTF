name:
Gravity Well

description:
You got jailed in a space station orbiting around a neutron star!
Can you overcome the gravitational pull to escape?
You have some control over the space station but its engine seems sealed away.
Wait... there is a stick guy floating around!
What's going on here?

author:
Pietro Lepori

public files:
server.py

---

flag:
KSUS{6561737465722065676773206172652066756e21f09fa59a}

---

parameters:
The server should be exposed on port 353 or ?0353

idea:
As the description says we have some control over the execution in the container:
- an environment variable
- a python script.
Our control is limited by the many tests on the input and the `-I` (isolated mode) flag.
The "stick guy floating around" is a reference to XKCD comic number 353.
One of Python easter eggs is the module `antigravity` (a convenient solution to a gravity well).
That module opens a webpage to the comic.
The imported `webbrowser` module uses the `BROWSER` environment variable.
That will be our attack point, payload:
`sh -c "cat flag.txt; echo %s"`
while the script can be the innocent looking
`import antigravity`
