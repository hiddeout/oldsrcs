from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from system import Marly


async def setup(bot: "Marly"):
    from .information import Information

    await bot.add_cog(Information(bot))
