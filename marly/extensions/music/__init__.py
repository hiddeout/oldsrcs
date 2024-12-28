from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from system import Marly


async def setup(bot: "Marly"):
    from .music import Music

    await bot.add_cog(Music(bot))