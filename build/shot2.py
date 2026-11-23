import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        errs=[]
        async def page(w,h,name,hash="",look="console",theme="dark"):
            ctx=await b.new_context(viewport={"width":w,"height":h})
            await ctx.add_init_script(f"localStorage.setItem('fa-look','{look}');localStorage.setItem('fa-theme','{theme}')")
            pg=await ctx.new_page()
            pg.on("pageerror",lambda e: errs.append(f"{name}: {e}"))
            pg.on("console",lambda m: errs.append(f"{name}: {m.text}") if m.type=="error" and "favicon" not in m.text and "404" not in m.text else None)
            await pg.goto("http://localhost:8765/index.html"+hash); await pg.wait_for_timeout(2000)
            await pg.screenshot(path=f"build/{name}.png"); await ctx.close()
        await page(1440,900,"c_console_83","#station-83")
        await page(1440,900,"c_midnight_all","","midnight")
        await page(1440,900,"c_reflective_72","#station-72","reflective")
        await page(1440,900,"c_console_light_68","#station-68","console","light")
        await page(390,844,"c_mob_mid_80","#station-80","midnight")
        await page(1440,900,"c_reflective_light_all","","reflective","light")
        print("\n".join(errs) or "no errors"); await b.close()
asyncio.run(main())
