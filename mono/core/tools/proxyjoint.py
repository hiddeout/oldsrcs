import asyncio
import random

async def get_proxy_ports():
    process = await asyncio.create_subprocess_exec(
        'netstat', '-tlnp',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if stderr:
        raise Exception(f"Error: {stderr.decode().strip()}")

    ports = []
    for line in stdout.decode().splitlines():
        if 'proxy-process' in line:
            parts = line.split()
            if len(parts) > 3:
                port_info = parts[3]
                port = port_info.split(':')[-1]  # Get the port number
                ports.append(port)

    return ports


async def get_random_proxy():
    ports = await get_proxy_ports()
    port = random.choice(ports)
    return f"http://admin:admin@127.0.0.1:{port}"