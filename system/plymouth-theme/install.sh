yay -S plymouth

yay -S plymouth-theme-aregression
sudo cp -r aregression/  /usr/share/plymouth/themes/
sudo cp mkinitcpio.conf /etc/
sudo cp grub /etc/default/
sudo mkinitcpio -P linux-zen; sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo systemctl enable lightdm.service
sudo cp plymouthd.conf /etc/plymouth/
sudo plymouth-set-default-theme -R aregression
