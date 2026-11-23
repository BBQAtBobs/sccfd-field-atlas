import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        errs=[]
        async def page(w,h,name,actions=None,theme=None):
            pg=await b.new_page(viewport={"width":w,"height":h},device_scale_factor=1)
            pg.on("console",lambda m: errs.append(f"{name}: {m.type}: {m.text}") if m.type in("error","warning") else None)
            pg.on("pageerror",lambda e: errs.append(f"{name}: PAGEERROR {e}"))
            await pg.goto("http://localhost:8765/index.html"+(actions or ""))
            await pg.wait_for_timeout(1800)
            if theme: 
                await pg.click("#theme"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"/home/claude/atlas/build/{name}.png")
            return pg
        await page(1440,900,"desk_dark")
        await page(1440,900,"desk_st83","#station-83")
        await page(1440,900,"desk_b68_light","#b68",theme=True)
        await page(390,844,"mob_over")
        await page(390,844,"mob_st72","#station-72")
        pg=await page(1440,900,"desk_search")
        await pg.fill("#q","t8"); await pg.wait_for_timeout(300); await pg.screenshot(path="/home/claude/atlas/build/desk_search.png")
        print("\n".join(errs) or "no console errors")
        await b.close()
asyncio.run(main())
