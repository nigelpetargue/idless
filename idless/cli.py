import click
import pyautogui
import time

@click.command()
@click.option('--wiggle', is_flag=True, help='Start the mouse wiggling')
@click.pass_context
def cli(ctx, wiggle):
    if wiggle:
        mouse_wiggler()
    else: 
        click.echo(ctx.get_help())

def mouse_wiggler():
    click.echo(click.style('Mouse wiggler started. Move your mouse manually to stop.', fg='green'))
    try:
        # Store the last position set by the script
        last_x, last_y = pyautogui.position()
        while True:
            # Automated movements
            for dx, dy in [(10, 0), (0, 10), (-10, 0), (0, -10)]:
                pyautogui.moveTo(last_x + dx, last_y + dy, duration=0.2)
                time.sleep(1)
                current_x, current_y = pyautogui.position()
                # If the mouse was moved manually (distance > 10 pixels), stop
                if abs(current_x - (last_x + dx)) > 10 or abs(current_y - (last_y + dy)) > 10:
                    click.echo(click.style('Mouse wriggler stopped (manual movement detected).', fg='red'))
                    return
                last_x, last_y = current_x, current_y
    except KeyboardInterrupt:
        click.echo(click.style('\nMouse wiggler stopped.', fg='red'))