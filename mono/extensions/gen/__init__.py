from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.Mono import Mono


async def setup(bot: "Mono"):
    from .information import Information

    await bot.add_cog(Information(bot))
