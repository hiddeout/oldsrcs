# **Mono-Skunkk Discord Bot**


## **Requirements**

- Python 3.12
- PostgreSQL
- Basic understanding of the terminal

## **Getting Started**

1. **Clone the Repository:**
   To get started, run the following command:

   ```bash
   git clone https://github.com/hiddeout/mono-opensource.git
   ```

2. **Install PostgreSQL:**
   Download and install PostgreSQL from [here](https://www.postgresql.org/download/windows/) or for your OS of choice.

3. **Create a Database:**
   Run the following command in your terminal or CMD:

   - For Linux:
     ```bash
     sudo -U postgres psql
     ```
   - For Windows:
     ```bash
     psql -U postgres
     ```

   Then inside the postgres terminal, run:

   ```sql
   CREATE DATABASE mono;
   ```


## **Install the Dependencies**

Open a terminal in this directory and run:

```bash
pyenv install 3.9.20
pyenv global 3.9.20
pip install -r requirements.txt
```

If this fails on windows make sure Python is installed and added to PATH.

Once installed, run:

```bash
python launcher.py
```

if you want to  contribute to the project, feel free to fork it and make a pull request.


## **Install And Setup Cloudflare Warped**

```bash
sudo apt-get update && sudo apt-get install cloudflare-warp -y 

warp-cli register
warp-cli set-mode proxy
warp-cli set-proxy-port 7483
warp-cli connect
```


## **Install Playwright After Installing Requirements**

```bash
playwright install
playwright install-deps
```


Source is based on "Kayo" by [Ethan](https://github.com/rxnk)

> Jail might not work , source is messy but it works. 🤷‍♂️
> also has userapps , that dont work on dm channels... works on other servers that the bot is not in tho




```python
@property
def guild_permissions(self) -> Permissions:
    """:class:`Permissions`: Returns the member's guild permissions.

    This only takes into consideration the guild permissions
    and not most of the implied permissions or any of the
    channel permission overwrites. For 100% accurate permission
    calculation, please use :meth:`abc.GuildChannel.permissions_for`.

    This does take into consideration guild ownership, the
    administrator implication, and whether the member is timed out.

    .. versionchanged:: 2.0
        Member timeouts are taken into consideration.
    """

    if self.guild.owner_id == self.id:
        return Permissions.all()

    base = Permissions.none()
    for r in self.roles:
        if r is not None:  # Ensure the role is not None
            base.value |= r.permissions.value

    if base.administrator:
        return Permissions.all()

    if self.is_timed_out():
        base.value &= Permissions._timeout_mask()

    return base
```
