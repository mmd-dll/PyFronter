from pyfronter import Html, render, run

html = Html()

page = html.html(
    html.head(
        html.meta(charset="UTF-8"),
        html.meta(name="viewport", content="width=device-width, in  itial-scale=1"),
        html.title("pyfronter - کتابخانه تولید HTML به سبک پایتون")
    ),
    html.body(
        html.header(
            html.h1("به pyfronter خوش آمدید").style(
                margin="0",
                font_size="2.5rem"
            ),
            html.nav(
                html.a("خانه", href="#home").style(
                    color="#e0e0e0",
                    text_decoration="none",
                    padding="8px 12px",
                    border_radius="4px",
                    transition="background 0.3s"
                ).on_hover(background_color="#333333"),
                html.a("ویژگی‌ها", href="#features").style(
                    color="#e0e0e0",
                    text_decoration="none",
                    padding="8px 12px",
                    border_radius="4px",
                    transition="background 0.3s"
                ).on_hover(background_color="#333333"),
                html.a("تماس", href="#contact").style(
                    color="#e0e0e0",
                    text_decoration="none",
                    padding="8px 12px",
                    border_radius="4px",
                    transition="background 0.3s"
                ).on_hover(background_color="#333333")
            ).style(
                display="flex",
                justify_content="center",
                gap="20px",
                margin_top="10px"
            )
        ).style(
            background_color="#1f1f1f",
            padding="20px",
            text_align="center",
            box_shadow="0 2px 5px rgba(0,0,0,0.5)"
        ),
        html.div(
            html.h2("ساخت HTML سریع و ساده با پایتون").style(
                font_size="1.8rem",
                margin_bottom="20px"
            ),
            html.p("pyfronter به شما اجازه می‌دهد صفحات HTML را با کد پایتون به صورت داینامیک بسازید و مدیریت کنید."),
            html.button("شروع استفاده از pyfronter").style(
                background_color="#bb86fc",
                color="#121212",
                border="none",
                padding="12px 24px",
                border_radius="25px",
                font_size="1rem",
                cursor="pointer",
                transition="background 0.3s"
            ).on_hover(background_color="#a46cf1"),
            class_="hero",
            id="home"
        ).style(
            padding="100px 20px",
            text_align="center",
            background="linear-gradient(135deg, #1f1f1f, #121212)"
        ),
        html.div(
            html.div(
                html.h3("کدنویسی ساده").style(
                    margin_top="0"
                ),
                html.p("ایجاد عناصر HTML بدون نیاز به نوشتن تگ‌های HTML به صورت دستی."),
                class_="card"
            ).style(
                background_color="#1f1f1f",
                padding="20px",
                border_radius="8px",
                box_shadow="0 2px 5px rgba(0,0,0,0.5)"
            ),
            html.div(
                html.h3("قابل توسعه").style(
                    margin_top="0"
                ),
                html.p("امکان ترکیب با سایر کتابخانه‌ها و چارچوب‌ها برای توسعه سریع."),
                class_="card"
            ).style(
                background_color="#1f1f1f",
                padding="20px",
                border_radius="8px",
                box_shadow="0 2px 5px rgba(0,0,0,0.5)"
            ),
            html.div(
                html.h3("تم تاریک پیش‌فرض").style(
                    margin_top="0"
                ),
                html.p("طراحی پیش‌فرض بر اساس تم تاریک، آماده استفاده برای پروژه‌های مدرن."),
                class_="card"
            ).style(
                background_color="#1f1f1f",
                padding="20px",
                border_radius="8px",
                box_shadow="0 2px 5px rgba(0,0,0,0.5)"
            ),
            class_="features",
            id="features"
        ).style(
            display="grid",
            grid_template_columns="repeat(auto-fit, minmax(200px, 1fr))",
            gap="20px",
            padding="40px 20px"
        ),
        html.div(
            html.h2("تماس با ما", id="contact"),
            html.form(
                html.input(type="text", name="name", placeholder="نام شما").style(
                    width="100%",
                    margin_bottom="10px",
                    padding="10px",
                    border_radius="6px",
                    border="1px solid #333",
                    background_color="#1f1f1f",
                    color="#e0e0e0"
                ),
                html.br(),
                html.input(type="email", name="email", placeholder="ایمیل شما").style(
                    width="100%",
                    margin_bottom="10px",
                    padding="10px",
                    border_radius="6px",
                    border="1px solid #333",
                    background_color="#1f1f1f",
                    color="#e0e0e0"
                ),
                html.br(),
                html.textarea(name="message", rows="4", placeholder="پیام شما").style(
                    width="100%",
                    margin_bottom="10px",
                    padding="10px",
                    border_radius="6px",
                    border="1px solid #333",
                    background_color="#1f1f1f",
                    color="#e0e0e0"
                ),
                html.br(),
                html.button("ارسال پیام", type="submit").style(
                    background_color="#bb86fc",
                    color="#121212",
                    border="none",
                    padding="12px 24px",
                    border_radius="25px",
                    font_size="1rem",
                    cursor="pointer",
                    transition="background 0.3s"
                ).on_hover(background_color="#a46cf1"),
                class_="card"
            ).style(
                background_color="#1f1f1f",
                padding="20px",
                border_radius="8px",
                box_shadow="0 2px 5px rgba(0,0,0,0.5)"
            ),
            class_="features"
        ).style(
            display="grid",
            grid_template_columns="1fr",
            gap="20px",
            padding="40px 20px"
        ),
        html.footer(
            html.p("© 2025 pyfronter. همه حقوق محفوظ است."),
            html.p("ساخته شده با ❤️ با پایتون")
        ).style(
            text_align="center",
            padding="20px",
            background_color="#1f1f1f",
            font_size="0.9rem"
        )
    ).style(
        margin="0",
        font_family="'Segoe UI', Tahoma, Arial, sans-serif",
        background_color="#121212",
        color="#e0e0e0",
        line_height="1.6"
    )
)

run(page)
