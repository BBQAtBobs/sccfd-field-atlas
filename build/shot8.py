import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
        errs=[]
        for look in ["console","midnight","reflective"]:
            ctx=await b.new_context(viewport={"width":1440,"height":900})
            await ctx.add_init_script(f"localStorage.setItem('fa-theme','light');localStorage.setItem('fa-look','{look}');localStorage.setItem('fa-layers',JSON.stringify({{hosp:true,lm:true,kinds:{{}}}}))")
            pg=await ctx.new_page(); pg.on("pageerror",lambda e: errs.append(str(e)))
            await pg.goto("http://localhost:8765/index.html"); await pg.wait_for_timeout(1600)
            await pg.screenshot(path=f"build/l_{look}_over.png")
            await pg.click("[data-fb=hosp]"); await pg.wait_for_timeout(300); await pg.screenshot(path=f"build/l_{look}_menu.png")
            await pg.click("[data-mv='hf:stemi']"); await pg.wait_for_timeout(1300)
            await pg.click("td button[data-place=GSH]"); await pg.wait_for_timeout(1300); await pg.screenshot(path=f"build/l_{look}_gsh.png")
            await pg.click("#tabs button[data-mode=study]"); await pg.wait_for_timeout(900); await pg.screenshot(path=f"build/l_{look}_study.png")
            await ctx.close()
        print("\n".join(errs) or "no errors"); await b.close()
asyncio.run(main())
