import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        errs=[]
        async def page(w,h,name,hash="",look="console",theme="dark",click=None):
            ctx=await b.new_context(viewport={"width":w,"height":h})
            await ctx.add_init_script(f"localStorage.setItem('fa-look','{look}');localStorage.setItem('fa-theme','{theme}')")
            pg=await ctx.new_page()
            pg.on("pageerror",lambda e: errs.append(f"{name}: {e}"))
            await pg.goto("http://localhost:8765/index.html"+hash); await pg.wait_for_timeout(1800)
            if click: await pg.click(click); await pg.wait_for_timeout(1200)
            await pg.screenshot(path=f"build/{name}.png"); await ctx.close()
        await page(1440,900,"d_trucks","#units-truck")
        await page(1440,900,"d_double","#units-double","midnight")
        await page(1440,900,"d_overview","","reflective",click="#seg button[data-bat=S72]")
        await page(1440,900,"d_over_all","","console")
        await page(390,844,"d_mob_rescue","#units-rescue","midnight")
        print("\n".join(errs) or "no errors"); await b.close()
asyncio.run(main())
